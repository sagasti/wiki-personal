#!/usr/bin/env python3
"""Fast-ish Apple travel mail scan for iCloud IMAP. No password printed."""
from __future__ import annotations

import email
import imaplib
import re
import socket
import sys
from email.header import decode_header
from email.utils import parsedate_to_datetime
from pathlib import Path

HOST = "imap.mail.me.com"
PORT = 993
USER = "sagasti@mac.com"
SECRETS = Path.home() / ".hermes/secrets/icloud-imap.env"
START_YEAR, END_YEAR = 1998, 2009
SOCK_TIMEOUT = 90


def load_pw() -> str:
    text = SECRETS.read_text(encoding="utf-8-sig", errors="replace")
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        if k.strip().upper() == "ICLOUD_IMAP_APP_PASSWORD":
            v = v.strip().strip("\"'").replace(" ", "")
            return v
    raise SystemExit(f"no ICLOUD_IMAP_APP_PASSWORD in {SECRETS}")


def dec_subj(raw) -> str:
    if not raw:
        return ""
    out = []
    for part, cs in decode_header(raw):
        if isinstance(part, bytes):
            out.append(part.decode(cs or "utf-8", errors="replace"))
        else:
            out.append(str(part))
    return "".join(out)


def p(msg: str) -> None:
    print(msg, flush=True)


def search(M: imaplib.IMAP4_SSL, criterion: str) -> set[str]:
    try:
        typ, data = M.search(None, criterion)
    except imaplib.IMAP4.error as e:
        p(f"  SEARCH fail [{criterion[:80]}]: {e}")
        return set()
    if typ != "OK" or not data or not data[0]:
        return set()
    return {x.decode() if isinstance(x, bytes) else str(x) for x in data[0].split() if x}


def main() -> None:
    socket.setdefaulttimeout(SOCK_TIMEOUT)
    pw = load_pw()
    p(f"login {USER}...")
    M = imaplib.IMAP4_SSL(HOST, PORT)
    M.sock.settimeout(SOCK_TIMEOUT)
    M.login(USER, pw)
    M.select("INBOX", readonly=True)
    p("login OK")

    # Phase 1: high-signal SUBJECT queries only (fast on iCloud)
    subjects = [
        "Trip Authorization",
        "International Travel Request",
        "Travel Authorization",
        "itinerary",
        "flight confirmation",
        "hotel reservation",
        "Part 2: Trip Authorization",
        "Travel Request",
        "travel.res",
    ]
    filters = [
        'FROM "@apple.com"',
        'TO "sagasti@apple.com"',
        'FROM "travel.res@apple.com"',
        'FROM "travel@"',
    ]

    ids: set[str] = set()
    n = 0
    for f in filters:
        for s in subjects:
            n += 1
            crit = f'({f} SUBJECT "{s}")'
            got = search(M, crit)
            if got:
                p(f"  [{n}] {len(got)} hits: {crit[:70]}")
            ids |= got
    p(f"unique ids after subject filters: {len(ids)}")

    # Phase 2: travel.res any mail (still subject-less but FROM-limited)
    for crit in (
        'FROM "travel.res@apple.com"',
        'FROM "travel.res"',
        'TO "sagasti@apple.com" FROM "@apple.com" SUBJECT "trip"',
        'TO "sagasti@apple.com" FROM "@apple.com" SUBJECT "travel"',
        'FROM "@apple.com" SUBJECT "trip"',
        'FROM "@apple.com" SUBJECT "Travel"',
        'FROM "@apple.com" SUBJECT "WWDC"',
        'FROM "@apple.com" SUBJECT "Road Tour"',
        'FROM "@apple.com" SUBJECT "Roadshow"',
        'FROM "@apple.com" SUBJECT "SummerCamp"',
        'FROM "@apple.com" SUBJECT "Channel Training"',
    ):
        n += 1
        got = search(M, crit)
        if got:
            p(f"  [{n}] {len(got)} hits: {crit[:70]}")
        ids |= got
    p(f"unique ids total: {len(ids)}")

    # Fetch headers only (small)
    rows = []
    for i, mid in enumerate(sorted(ids, key=lambda x: int(x) if x.isdigit() else 0), 1):
        if i % 50 == 0:
            p(f"  fetch headers {i}/{len(ids)}...")
        try:
            typ, data = M.fetch(mid, "(BODY.PEEK[HEADER.FIELDS (DATE SUBJECT FROM TO CC)])")
            if typ != "OK" or not data or not data[0] or not isinstance(data[0], tuple):
                continue
            raw = data[0][1]
            if not isinstance(raw, (bytes, bytearray)):
                continue
            msg = email.message_from_bytes(raw)
            subj = dec_subj(msg.get("subject"))
            fr = msg.get("from") or ""
            date_hdr = msg.get("date")
            try:
                dt = parsedate_to_datetime(date_hdr) if date_hdr else None
            except Exception:
                dt = None
            if dt and (dt.year < START_YEAR or dt.year > END_YEAR):
                continue
            rows.append(
                {
                    "id": mid,
                    "date": dt.isoformat() if dt else "?",
                    "year": dt.year if dt else None,
                    "subject": subj,
                    "from": fr,
                    "to": msg.get("to") or "",
                }
            )
        except Exception as e:
            p(f"  fetch err id={mid}: {e}")
            continue

    try:
        M.logout()
    except Exception:
        pass

    p(f"\n=== RESULTS {len(rows)} messages in {START_YEAR}-{END_YEAR} ===")
    rows.sort(key=lambda r: r["date"])

    by_year: dict[int, int] = {}
    for r in rows:
        y = r["year"] or 0
        by_year[y] = by_year.get(y, 0) + 1
    p("by year: " + ", ".join(f"{y}:{c}" for y, c in sorted(by_year.items())))

    out_path = Path("/tmp/viajes_apple_result.txt")
    with out_path.open("w", encoding="utf-8") as f:
        f.write(f"# Apple travel-related mail scan {START_YEAR}-{END_YEAR}\n")
        f.write(f"# count={len(rows)}\n\n")
        for r in rows:
            line = (
                f"{r['date'][:10] if r['date'] != '?' else '?'} | "
                f"{(r['subject'] or '')[:100]} | "
                f"{(r['from'] or '')[:50]} | id={r['id']}\n"
            )
            f.write(line)
            print(line.rstrip(), flush=True)

    # copy to Desktop for Jorge
    desk = Path.home() / "Desktop" / "viajes_apple_result.txt"
    try:
        desk.write_text(out_path.read_text(encoding="utf-8"), encoding="utf-8")
        p(f"\nwrote {out_path} and {desk}")
    except Exception as e:
        p(f"\nwrote {out_path} (desktop copy failed: {e})")


if __name__ == "__main__":
    main()

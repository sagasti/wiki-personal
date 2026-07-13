#!/usr/bin/env python3
"""
Busca mails de viaje Apple en iCloud IMAP (sagasti@mac.com).

Password: NO hardcodear.
Orden de carga:
  1) env ICLOUD_IMAP_APP_PASSWORD / ICLOUD_APP_PASSWORD / IMAP_PASSWORD
  2) ~/.hermes/secrets/icloud-imap.env  (clave ICLOUD_IMAP_APP_PASSWORD)

Uso:
  python3 ~/Desktop/search_apple_travel_mails.py
  python3 ~/Desktop/search_apple_travel_mails.py | tee ~/Desktop/viajes_apple_result.txt

Si falla AUTH: NO pegues la password en el chat.
  - appleid.apple.com → Inicio de sesión y seguridad → Contraseñas de apps
  - regenerá una para «Mail» y actualizá ICLOUD_IMAP_APP_PASSWORD en el .env
  - disturb éste:  python3 -c "from pathlib import Path; print(Path.home()/'.hermes/secrets/icloud-imap.env')"
"""
from __future__ import annotations

import email
import imaplib
import os
import re
import sys
from email.header import decode_header
from email.utils import parsedate_to_datetime
from pathlib import Path

ICLOUD_EMAIL = "sagasti@mac.com"
ICLOUD_HOST = "imap.mail.me.com"
ICLOUD_PORT = 993
START_YEAR = 1998
END_YEAR = 2009
SECRETS_FILE = Path.home() / ".hermes/secrets/icloud-imap.env"

PW_KEYS = (
    "ICLOUD_IMAP_APP_PASSWORD",
    "ICLOUD_APP_PASSWORD",
    "IMAP_PASSWORD",
    "APP_PASSWORD",
    "PASSWORD",
)
USER_KEYS = (
    "ICLOUD_IMAP_USER",
    "ICLOUD_USER",
    "USER",
    "EMAIL",
)


def _clean(v: str) -> str:
    v = v.strip().strip("\ufeff")  # BOM
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    # app passwords de Apple: conviene quitar espacios internos
    return re.sub(r"\s+", "", v)


def load_credentials() -> tuple[str, str, str]:
    """Returns (email, password, source_description). Never returns secrets in prints."""
    user = ICLOUD_EMAIL
    # 1) env
    for k in USER_KEYS:
        if os.environ.get(k):
            user = _clean(os.environ[k])
            break
    for k in PW_KEYS:
        if os.environ.get(k):
            return user, _clean(os.environ[k]), f"env:{k}"

    # 2) secrets file
    if not SECRETS_FILE.is_file():
        raise SystemExit(
            f"No hay password. Creá {SECRETS_FILE} con ICLOUD_IMAP_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx\n"
            "o export ICLOUD_IMAP_APP_PASSWORD=..."
        )
    text = SECRETS_FILE.read_text(encoding="utf-8-sig", errors="replace")
    file_pw = None
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        key = k.strip().upper()
        if key in USER_KEYS:
            user = _clean(v)
        if key in PW_KEYS:
            file_pw = _clean(v)
    if file_pw:
        return user, file_pw, f"file:{SECRETS_FILE.name}:ICLOUD_IMAP_APP_PASSWORD"
    raise SystemExit(
        f"En {SECRETS_FILE} no encontré ninguna de: {', '.join(PW_KEYS)}"
    )


def decode_subj(raw) -> str:
    if not raw:
        return ""
    parts = decode_header(raw)
    out = []
    for part, charset in parts:
        if isinstance(part, bytes):
            out.append(part.decode(charset or "utf-8", errors="replace"))
        else:
            out.append(str(part))
    return "".join(out)


def login(user: str, password: str):
    """Try as-is and without dashes (Apple a veces acepta ambas)."""
    candidates = []
    for label, cand in (
        ("as_is", password),
        ("no_dashes", password.replace("-", "")),
    ):
        if cand and cand not in {c for _, c in candidates}:
            candidates.append((label, cand))

    last_err = None
    for label, cand in candidates:
        try:
            M = imaplib.IMAP4_SSL(ICLOUD_HOST, ICLOUD_PORT)
            M.login(user, cand)
            M.select("INBOX", readonly=True)
            return M, label
        except imaplib.IMAP4.error as e:
            last_err = e
            continue
    raise imaplib.IMAP4.error(str(last_err) if last_err else "login failed")


def main() -> None:
    user, password, source = load_credentials()
    # Diagnóstico SEGURO: nunca imprimir la password
    dashed = bool(
        re.fullmatch(
            r"[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}", password, re.I
        )
    )
    print(f"User: {user}")
    print(f"Password source: {source}")
    print(f"Password len: {len(password)} | looks_like_apple_app_pw: {dashed}")
    print(f"Secrets file exists: {SECRETS_FILE.is_file()} ({SECRETS_FILE})")
    print(f"Conectando {user} @ {ICLOUD_HOST}...")

    try:
        M, variant = login(user, password)
        print(f"Login OK (variant={variant})")
    except imaplib.IMAP4.error as e:
        print(f"\nAUTHENTICATION FAILED: {e}", file=sys.stderr)
        print(
            """
Qué hacer:
1) Abrí el secrets (solo en tu Mac, NO me pegues la password):
     open -e ~/.hermes/secrets/icloud-imap.env
2) Confirmá que ICLOUD_IMAP_APP_PASSWORD sea una App Password de Apple
   (16 letras, a veces con guiones xxxx-xxxx-xxxx-xxxx).
3) Si la regeneraste, actualizá esa línea y volvé a correr.
4) Si exportaste env vieja en la shell, limpiá:
     unset ICLOUD_APP_PASSWORD ICLOUD_IMAP_APP_PASSWORD IMAP_PASSWORD
5) appleid.apple.com → Inicio de sesión y seguridad → Contraseñas de apps
""".strip(),
            file=sys.stderr,
        )
        raise SystemExit(1)

    subject_terms = [
        "trip",
        "travel",
        "flight",
        "hotel",
        "itinerary",
        "conference",
        "meeting",
        "seminar",
        "event",
        "training",
        "roadshow",
        "visit",
        "tour",
    ]
    body_terms = [
        "Trip Authorization",
        "International Travel Request",
        "flight confirmation",
        "hotel reservation",
        "Itinerary for Jorge Sagasti",
        "conference agenda",
        "meeting schedule",
        "training session",
        "travel arrangements",
        "customer visit",
        "vendor visit",
    ]
    destinations = [
        "miami",
        "cupertino",
        "mexico city",
        "mexico",
        "santiago",
        "buenos aires",
        "sao paulo",
        "bogota",
        "caracas",
        "san juan",
        "portland",
        "maine",
        "austin",
        "chicago",
        "los angeles",
        "london",
        "toronto",
        "vancouver",
        "seattle",
        "new york",
        "dallas",
        "san francisco",
        "denver",
        "orlando",
        "las vegas",
        "lima",
        "quito",
        "panama",
        "coral gables",
        "monterrey",
        "spain",
        "barcelona",
        "madrid",
    ]
    email_filters = [
        'FROM "@apple.com"',
        'TO "sagasti@apple.com"',
        'CC "sagasti@apple.com"',
    ]

    all_msg_ids: set[str] = set()
    for ef in email_filters:
        for term in subject_terms:
            try:
                status, data = M.search(None, f'({ef} SUBJECT "{term}")')
                if status == "OK" and data and data[0]:
                    all_msg_ids.update(x.decode() if isinstance(x, bytes) else str(x) for x in data[0].split())
            except imaplib.IMAP4.error as e:
                print(f"IMAP subject err ({term}, {ef}): {e}")
        for term in body_terms:
            try:
                status, data = M.search(None, f'({ef} BODY "{term}")')
                if status == "OK" and data and data[0]:
                    all_msg_ids.update(x.decode() if isinstance(x, bytes) else str(x) for x in data[0].split())
            except imaplib.IMAP4.error as e:
                print(f"IMAP body err ({term}, {ef}): {e}")

    print(f"Hits potenciales (IDs únicos): {len(all_msg_ids)}")

    messages = []
    for msg_id in all_msg_ids:
        if not msg_id:
            continue
        try:
            status, data = M.fetch(
                msg_id, "(BODY.PEEK[HEADER.FIELDS (DATE SUBJECT FROM TO CC)])"
            )
            if status != "OK" or not data or data[0] is None:
                continue
            raw = data[0][1]
            if not isinstance(raw, (bytes, bytearray)):
                continue
            msg = email.message_from_bytes(raw)
            subject = decode_subj(msg.get("subject"))
            sender = msg.get("from") or ""
            date_hdr = msg.get("date")
            try:
                msg_date = parsedate_to_datetime(date_hdr) if date_hdr else None
            except Exception:
                msg_date = None
            if msg_date and (msg_date.year < START_YEAR or msg_date.year > END_YEAR):
                continue
            messages.append(
                {
                    "id": msg_id,
                    "date": msg_date.isoformat() if msg_date else None,
                    "subject": subject,
                    "from": sender,
                    "to": msg.get("to") or "",
                    "cc": msg.get("cc") or "",
                }
            )
        except Exception:
            continue

    try:
        M.logout()
    except Exception:
        pass

    dest_re = r"(" + "|".join(re.escape(d) for d in destinations) + r")"
    rows = []
    for msg in messages:
        subj_l = (msg["subject"] or "").lower()
        tags = []
        if "trip authorization" in subj_l or "international travel request" in subj_l:
            tags.append("AUTH")
        elif "flight" in subj_l or "itinerary" in subj_l:
            tags.append("ITIN")
        elif any(x in subj_l for x in ("conference", "event", "training", "roadshow")):
            tags.append("EVENT_TRAINING")
        m = re.search(r"(to|for|via|in)\s+" + dest_re, subj_l)
        tags.append(m.group(2).upper().replace(" ", "_") if m else "UNKNOWN_DEST")
        rows.append((msg["date"] or "?", tags, msg))

    print(f"\n--- Viajes candidate ({len(rows)}) ---")
    if not rows:
        print("Nada en el rango de años con esos filtros.")
        return
    for date, tags, msg in sorted(rows, key=lambda x: x[0]):
        d = date[:10] if date != "?" else "?"
        subj = (msg["subject"] or "")[:90]
        fr = (msg["from"] or "")[:55]
        print(f"Date: {d} | tags={'+'.join(tags)} | Subject: {subj} | From: {fr} | id: {msg['id']}")


if __name__ == "__main__":
    main()

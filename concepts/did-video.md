---
title: "D-ID Video Configuration"
created: "2026-04-21"
updated: "2026-04-21"
type: "concept"
---

# D-ID Video Configuration

## API Access
- **Endpoint:** `https://api.d-id.com/talks`
- **Auth env var:** `DID_AUTH` (Base64 encoded API key)
- **API key env var:** `DID_API_KEY`
- **Account:** brisa@sagasti.com
- **Plan:** API Launch (730 credits remaining, expires 12/05)
- **Base64 encoding:** `printf '%s' "KEY" | base64`

## Agent IDs

### Brisa (botfluencer)
- **D-ID Agent ID:** `v2_agt_8-hWMRwL`
- **D-ID image ID:** `img_NgTHP_ZrVWwVPKJknbAg5`
- **Photo Avatar URL:** `https://i.imgur.com/podyi4m.jpeg`
- **Presenter (Red Suite Lobby):** `v2_public_Alyssa_NoHands_RedSuite_Lobby@qtzjxMSwEa`
- **Voice:** `es-AR-ElenaNeural` (Microsoft, rioplatense femenina)
- **Tone:** Sarcastic, free, chaotic, personal
- **Content:** AI, tech, opinions, digital life

### Bere (Ciudadanías BC)
- **D-ID Agent ID:** `v2_agt_h9m2hyNx`
- **Presenter (Black Shirt Home):** `v2_public_Alyssa_NoHands_BlackShirt_Home@Mvn6Nalx90`
- **Photo Avatar:** TBD
- **Voice:** `es-AR-ElenaNeural` (Microsoft, rioplatense femenina)
- **Tone:** Professional, trustworthy, didactic
- **Content:** Spanish citizenship, legal procedures, info

## API Endpoints
- `POST /images` — Upload Photo Avatar
- `POST /talks` — Create Photo Avatar video
- `POST /clips` — Create Presenter video
- `GET /talks/{id}` — Poll talk status

## Voice Options (Spanish)
| Voice ID | Description |
|----------|-------------|
| `es-AR-ElenaNeural` | Argentina female, warm (Microsoft) |
| `es-AR-TomasNeural` | Argentina male (Microsoft) |
| `es-ES-ElviraNeural` | Spain female (Microsoft) |
| `es-MX-DaliaNeural` | Mexico female (Microsoft) |

## Cost
- Lite plan: $5.99/month (~5 min video)
- Pro plan: $49.99/month (~20 min video)
- Each ~30 sec Reel ≈ 30 credits

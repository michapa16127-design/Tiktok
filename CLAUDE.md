# NovaAxis – Projektgedächtnis (damit keine Sitzung bei null anfängt)

Stand: 14.10.2026. Lies diese Datei zuerst. Sprache mit dem Nutzer: Deutsch, „du“.

## Produkt
NovaAxis „Angst wandeln in Vertrauen“. Produktlink: **https://app.novaaxis.org/**
Ablauf: Gratis-Test (30 Fragen, ca. 10 Min., nur Vorname + E-Mail) → Auswertung → 7-Tage-Programm, 9,99 € einmalig, lebenslanger Zugang, Online-Tagebuch im Browser.
Gründer: Michael Paul (Osteopath, Qi-Gong-Trainer, Fitness, Prävention – laut seiner YouTube-Beschreibung).
Nische (Hypothese): Anspannung/Angst bei Job-/KI-Stress im Körper lösen, Berufstätige 35–55, DACH. Siehe `novaaxis/ANALYSE_ABSCHLUESSE.md`.

## Konten
- TikTok: **@NovaAxisWandel** (NICHT @wirbelsaeulengesundheit – dort liegt versehentlich das Erklärvideo)
- YouTube: Kanal „Michael Paul NovaAxis“, ID UC7AzKcT1quug9dNCaPAHcFA (bei vidIQ verbunden)
- Instagram, Facebook, LinkedIn: Handles noch eintragen → ______

## Regeln für jeden Post (nicht neu fragen)
1. **Zwei Folien** (Inhalt + Link), **ruhige Musik** als 15-s-Video, dazu Bild-Karussell.
2. **Link in der Bio** (letzte Folie + Caption) und **Link unten** (Fußzeile jeder Folie: app.novaaxis.org).
3. **5 Hashtags**, ein Hashtag `#novaaxis`.
4. Facebook/LinkedIn: Link direkt in den Text (dort klickbar). TikTok/Instagram: nur Bio-Link klickbar.
5. Keine Heilversprechen, keine erfundenen Erfahrungsberichte; bei Herzrasen/Schmerzen Arzt-Hinweis.
6. **Sprachen:** Laut Nutzer gibt es das Programm in **6 Sprachen** (welche, und wie die Sprachversion gewählt wird, ist noch zu klären → siehe `novaaxis/social/MEHRSPRACHIG.md`). Frühere Annahme „die Seite ist deutsch“ war ungeprüft und ist zu verwerfen. Pro Sprache ein eigenes Konto und ein eigener Bio-Link zur passenden Sprachversion.

## Wenn der Nutzer eine Idee sagt
1. `python3 novaaxis/social/new_post.py ...` (siehe `.claude/skills/novaaxis-post/SKILL.md`) → Folien, Video, Caption.
2. Posten/Planen über den verbundenen Planungs-Konnektor (Metricool: `createScheduledPost`), wenn verbunden. Sonst: Auftrag für den Chrome-Chat in `novaaxis/social/AUFTRAG_BROWSER_POSTEN.md`.
3. Nie behaupten, etwas sei gepostet, wenn nur Dateien erstellt wurden. Immer sagen, was wirklich passiert ist.

## Verbindungen (Stand 14.10.2026)
| Dienst | Status |
|---|---|
| vidIQ | verbunden (YouTube-Kanal verbunden, Instagram NICHT; Änderungen an Videos brauchen Google-MFA) |
| Google Drive, Gmail | verbunden |
| TikTok for Business | verbunden, aber **kein Werbekonto** → nur Werbung, kein Posten |
| **Metricool** (TikTok, Instagram, Facebook, LinkedIn, YouTube planen) | **NICHT verbunden – Haupt-To-do** |
| Claude in Chrome (Desktop-App) | nur in Desktop-Chat, nicht in Cloud-Sitzungen |

## Bekannte Grenzen (nicht noch einmal ausprobieren)
- Cloud-Sitzung hat kein Chrome. Netzwerk blockiert tiktok.com, drive.google.com, app.novaaxis.org.
- Drive-Werkzeug liefert Dateien nur als Text in den Chat → Videos/Bilder nicht übertragbar (GitHub-Repo nutzen).
- TikTok-Kurzlinks (vm.tiktok.com) lassen sich nicht auswerten, nur volle `/@name/video/ID`-Links.

## Wichtige Dateien
`novaaxis/social/` – `README.md`, `WOCHE2_PLAN.md`, `LINKS.md`, `SPIELPLAN_HEUTE.md`, `AUFTRAG_BROWSER_POSTEN.md`, `make_carousels.py`, `make_slide_videos.py`, `new_post.py`, `carousels*.json`, `music/`.
Strategie: `novaaxis/STRATEGIE.md`, `novaaxis/INSTAGRAM_10_POSTS.md`.
Video C0043 (Google Drive, 369 MB) wartet auf Transkript für türkische Untertitel (Weg: YouTube „Nicht gelistet“).

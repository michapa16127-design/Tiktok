# Earnings Tracker

Kleines CLI-Tool (nur Python-Standardbibliothek, keine Installation nötig),
um Stunden und Verdienst je Plattform zu loggen und daraus den **echten
effektiven Stundenlohn** zu berechnen — die Zahl, die im Video fehlt.

```bash
# Session eintragen (USD-Plattformen: Kurs des Auszahlungstages angeben)
python3 tracker.py add --platform Outlier --date 2026-09-12 \
  --hours 1.5 --earnings-usd 32.50 --eur-rate 0.92 --tasks 14

# Session in EUR (z. B. Clickworker)
python3 tracker.py add --platform Clickworker --date 2026-09-12 \
  --hours 1.0 --earnings-eur 8.40

# Report über alle Plattformen
python3 tracker.py report

# Report nur für eine Plattform
python3 tracker.py report --platform Outlier
```

Daten liegen als einfache CSV unter `data/sessions.csv` — bewusst kein
Datenbank-Overhead, damit du sie jederzeit direkt in Excel/Numbers öffnen
oder als Beleggrundlage für die Steuer exportieren kannst (siehe
`../germany-gewerbe-steuern.md`).

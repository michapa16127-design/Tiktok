# Tiktok

Analyse und Nachbau des Referenzvideos (Creator `@stealth.strategy_`, Hook
*"23-Jähriger kündigt seinen Job wegen Mini-AI Aufgaben (789€ pro Tag)"*).

Zwei Teile:

- **[`business/`](business/)** — das reale Geschäftsmodell aus dem Video
  ("Mini-AI-Aufgaben" = bezahlte KI-Trainingsdaten-Microtasks) zum
  Selbermachen: Plattform-Vergleich, 30-Tage-Einstiegsplan,
  Gewerbe/Steuer-Einordnung für Deutschland, und ein Tracking-Tool für
  deinen echten effektiven Stundenlohn.
  - [`mini-ai-tasks.md`](business/mini-ai-tasks.md) — Einstiegspunkt/Übersicht
  - [`platforms.md`](business/platforms.md) — welche Plattform lohnt sich
  - [`getting-started.md`](business/getting-started.md) — Schritt-für-Schritt
  - [`germany-gewerbe-steuern.md`](business/germany-gewerbe-steuern.md)
  - [`earnings_tracker/`](business/earnings_tracker/) — CLI-Tool für dein
    €/h-Tracking über alle Plattformen hinweg
- **[`viral_caption_tool/`](viral_caption_tool/)** — das
  Content-Produktionswerkzeug: erzeugt aus jedem Talking-Head-Video +
  Skript denselben visuellen Stil wie im Referenzvideo (Hook-Banner oben,
  fette Wort-für-Wort-Captions, Handle-Wasserzeichen), falls du deine
  Erfahrungen damit auch als Content dokumentieren willst.

Schnellstart:

```bash
cd viral_caption_tool
python3 make_viral_clip.py \
  --video dein_video.mp4 \
  --srt   dein_skript.srt \
  --hook  "Deine Schlagzeile" \
  --handle "@dein.handle" \
  --out   fertig.mp4
```

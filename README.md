# Tiktok

Analyse und Nachbau des Referenzvideos (Creator `@stealth.strategy_`, Hook
*"23-Jähriger kündigt seinen Job wegen Mini-AI Aufgaben (789€ pro Tag)"*).

Zwei Teile:

- **[`viral_caption_tool/`](viral_caption_tool/)** — das eigentliche,
  wiederverwendbare Produktionswerkzeug: erzeugt aus jedem
  Talking-Head-Video + Skript denselben visuellen Stil wie im Referenzvideo
  (Hook-Banner oben, fette Wort-für-Wort-Captions, Handle-Wasserzeichen).
- **[`business/mini-ai-tasks.md`](business/mini-ai-tasks.md)** — ehrliche
  Einordnung des im Video beworbenen Geschäftsmodells ("Mini-AI-Aufgaben")
  plus der dahinterliegenden Content-Formel, falls du das Format für ein
  eigenes, reales Angebot nutzen willst.

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

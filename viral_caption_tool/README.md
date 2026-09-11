# Viral Caption Tool

Rekonstruiert das Produktionssystem aus dem analysierten Referenz-Clip
(`@stealth.strategy_`, Hook: *"23-Jähriger kündigt seinen Job wegen Mini-AI
Aufgaben (789€ pro Tag)"*) als wiederverwendbares Werkzeug: aus jedem
Talking-Head-Video + Skript erzeugt es exakt denselben visuellen Aufbau.

## Was am Original repliziert wurde

| Element | Beobachtung im Referenzvideo | Umsetzung hier |
|---|---|---|
| Hook-Banner | Weiße abgerundete Box, fetter schwarzer Text, oben ~17% der Höhe | `hook_banner.py` – PIL rendert die Box automatisch textgroß |
| Captions | Ein Wort (teils zwei) auf einmal, fett, weiß mit dicker schwarzer Kontur, unteres mittleres Drittel, hart getimt auf die Sprache | `build_ass.py` – generiert `.ass`-Untertitel, Burn-in via `libass` |
| Handle | Kleines fettes `@handle` unten links mit Schatten | `hook_banner.render_handle` |
| Schnitttempo / Perspektivwechsel | Häufige Jump-Cuts Sitzen/Stehen | bewusst nicht automatisiert – das ist Aufnahme-Regie, kein Post-Effekt |
| Format | 9:16 vertikal | Tool übernimmt die Auflösung des Eingabevideos |

## Voraussetzungen

- `ffmpeg` mit `libass`-Unterstützung (`ffmpeg -filters | grep ass`)
- Python 3.10+, `pip install -r requirements.txt` (Pillow)

## Nutzung

```bash
python3 make_viral_clip.py \
  --video dein_talking_head.mp4 \
  --srt   dein_skript.srt \
  --hook  "Deine Schlagzeile hier" \
  --handle "@dein.handle" \
  --out   fertig.mp4
```

- `--srt` kann normale (satzweise) Untertitel enthalten – die Wörter werden
  automatisch zeitlich anteilig aufgeteilt. Hast du bereits wortgenaue
  Timings (z. B. aus CapCut- oder Whisper-Export), funktioniert das direkt.
- `--chunk 2` zeigt zwei Wörter gleichzeitig statt eins (etwas ruhigeres Tempo).
- Erzeugen eigener Untertitel: jedes Tool, das `.srt` exportiert, reicht
  (CapCut, YouTube Auto-Captions, Descript, ein lokal installiertes
  Whisper). In dieser Sandbox war der Modell-Download für automatische
  Spracherkennung durch die Netzwerk-Policy blockiert, daher erwartet das
  Tool eine fertige `.srt` als Eingabe statt selbst zu transkribieren.

## Beispiel

`examples/example.srt` + ein synthetisches Testvideo zeigen die Pipeline
end-to-end (`examples/output_demo.mp4`, `check1.png`/`check2.png` als
Stichproben-Frames).

## Das Geschäftsmodell im Video

Siehe [`../business/mini-ai-tasks.md`](../business/mini-ai-tasks.md) für die
Einordnung des inhaltlichen Angebots ("Mini-AI-Aufgaben") und wie man damit
seriös startet.

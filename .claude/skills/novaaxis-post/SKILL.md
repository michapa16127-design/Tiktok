---
name: novaaxis-post
description: Erstellt aus einer Idee einen fertigen NovaAxis-Post (2 Folien, Musik-Video, Caption, Hashtags, Link) und plant ihn über den verbundenen Konnektor. Nutzen, wenn der Nutzer sagt „ich habe eine Idee“, „poste das“ oder einen neuen Social-Media-Beitrag für NovaAxis will.
---

1. Lies `CLAUDE.md` (Regeln, Konten, Link).
2. Formuliere aus der Idee: Kicker (Thema, groß), Titel (Hook, max. ~8 Wörter), Text (1–2 Sätze), CTA-Titel, CTA-Text. Körpersymptome → Arzt-Hinweis in den Text.
3. Erzeuge den Post:
```
python3 novaaxis/social/new_post.py --slug 18_thema --kicker "…" --title "…" --text "…" \
  --cta-title "…" --cta-text "Kostenloser Test · 30 Fragen · 10 Min." \
  --caption "Ein Satz für die Caption" --hashtags "#a #b #c #d #novaaxis"
```
   Ergebnis in `novaaxis/social/posts/<slug>/` (Bilder), `<slug>_9x16/` (Bilder + `zwei_folien_musik.mp4`) und `POST.md` (Captions).
4. Sieh dir mindestens eine Folie an (Read auf die PNG), bevor du sie weitergibst.
5. Planen/Posten: Wenn ein Planungs-Konnektor (z. B. Metricool) verbunden ist, lade ihn per ToolSearch und plane für TikTok, Instagram, Facebook, LinkedIn mit den Texten aus `POST.md` (Facebook/LinkedIn mit klickbarem Link). Vor dem Planen kurz Konto, Uhrzeit und Caption nennen. Wenn keiner verbunden ist: sage das klar und gib den Auftrag aus `novaaxis/social/AUFTRAG_BROWSER_POSTEN.md`.
6. Committe und pushe die neuen Dateien auf den Arbeits-Branch.
7. Berichte ehrlich: erstellt, geplant (wo, wann) oder nur vorbereitet.

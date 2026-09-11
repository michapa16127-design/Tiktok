# Gewerbe & Steuern in Deutschland — Orientierung, keine Rechtsberatung

Diese Microtask-Plattformen sind fast immer ausländische (meist US-)
Unternehmen ohne deutschen Lohnsteuerabzug. Das heißt: **du bist damit
automatisch selbständig tätig**, keine Lohnsteuer wird für dich abgeführt —
du musst dich selbst darum kümmern. Nachfolgend nur eine Orientierung; für
deine konkrete Situation (insbesondere Schwellenwerte, die sich ändern
können) einen **Steuerberater** oder die Existenzgründungsberatung der
IHK/des Finanzamts konsultieren.

## Grundsätzliches

- **Nebenberuflich vs. hauptberuflich**: solange es neben Ausbildung/Job
  ein Nebenverdienst bleibt, ändert das nichts an der grundsätzlichen
  Pflicht zur Anmeldung — es beeinflusst aber Kranken-/Sozialversicherung
  und ggf. IHK-Beitrag.
- **Gewerbeanmeldung**: regelmäßige, auf Gewinn ausgerichtete Tätigkeit ist
  in der Regel eine gewerbliche Tätigkeit → Anmeldung beim Gewerbeamt
  deiner Stadt/Gemeinde (Online-Formular oder vor Ort, geringe Gebühr).
  Ein einmaliger Testmonat vor der Anmeldung ist in der Praxis meist
  unkritisch — aber sobald daraus ein fortlaufender Nebenverdienst wird,
  gehört das angemeldet.
- **Finanzamt**: nach Anmeldung bekommst du automatisch den "Fragebogen
  zur steuerlichen Erfassung" (auch direkt über ELSTER möglich) — darin
  gibst du deine geschätzten Einkünfte an.
- **Kleinunternehmerregelung (§19 UStG)**: bei niedrigem Jahresumsatz
  kannst du dich von der Umsatzsteuerpflicht befreien lassen (keine USt.
  auf Rechnungen, aber auch kein Vorsteuerabzug). Die genauen
  Umsatzgrenzen ändern sich gesetzlich — **aktuellen Stand beim
  Finanzamt/Steuerberater prüfen**, nicht auf alte Zahlen verlassen.
- **Einkommensteuer**: die Einnahmen aus den Plattformen zählst du als
  Gewinn aus Gewerbebetrieb (Einnahmen-Überschuss-Rechnung reicht bei
  diesen Größenordnungen i. d. R. aus) in deiner Steuererklärung an —
  Belege/Auszahlungsnachweise aufheben.

## Praktisch wichtig bei US-Auszahlungen

- Auszahlungen kommen meist in **USD** — für die Steuer brauchst du den
  EUR-Gegenwert zum jeweiligen Zahlungsdatum (Wise/PayPal-Abrechnung
  liefert das i. d. R. automatisch, sonst EZB-Referenzkurs des Tages
  nutzen).
- Alle Auszahlungs-PDFs/CSV-Exports der Plattformen sammeln — Basis für
  deine EÜR und im Zweifel Nachweis gegenüber dem Finanzamt.
- Der `earnings_tracker/` in diesem Repo speichert Betrag + Datum je
  Session strukturiert ab — exportiere die CSV regelmäßig als Backup
  deiner Buchhaltungsgrundlage.

## Checkliste

- [ ] Testphase (siehe `getting-started.md`) durchlaufen, prüfen ob es sich
      lohnt fortzusetzen
- [ ] Bei Fortsetzung: Gewerbe anmelden
- [ ] Fragebogen zur steuerlichen Erfassung ausfüllen (ELSTER)
- [ ] Entscheidung Kleinunternehmerregelung ja/nein mit Steuerberater klären
- [ ] Ablagesystem für Auszahlungsnachweise einrichten (z. B. Ordner pro
      Kalenderjahr, `earnings_tracker`-CSV als Ergänzung)

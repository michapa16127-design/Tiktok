# Dauerhafte Verbindung: TikTok, Instagram, Facebook, LinkedIn (einmalig, ca. 20 Min.)

Ziel: Du sagst „Idee: …“, und der Post wird erstellt und in allen vier Kanälen geplant, ohne Rückfragen.
Werkzeug: **Metricool** (plant TikTok, Instagram, Facebook, LinkedIn und YouTube; als Claude-Konnektor verfügbar).
Die Anmeldungen bei den Netzwerken kann nur du selbst machen. Alles andere erledigt der Konnektor.

## Voraussetzungen (vorher prüfen)
- **Instagram:** Konto auf „Professionell“ (Business oder Creator) umstellen und mit einer **Facebook-Seite** verknüpfen.
- **Facebook:** Es muss eine **Seite** sein (nicht nur das private Profil).
- **TikTok:** Konto @NovaAxisWandel (Business- oder Creator-Konto empfohlen).
- **LinkedIn:** Profil oder Unternehmensseite – in Metricool prüfen, was dein Tarif unterstützt.

## Schritte
1. Konto bei Metricool anlegen (Tarif und Grenzen dort prüfen, vor allem Anzahl Netzwerke und Beiträge pro Monat).
2. In Metricool eine Marke „NovaAxis“ anlegen und die vier Netzwerke verbinden (jeweils bei dem Netzwerk anmelden und erlauben).
3. In claude.ai: **Einstellungen → Konnektoren → Metricool hinzufügen** und anmelden.
4. Neue Sitzung starten und schreiben: „Metricool ist verbunden.“

## Was ich danach als Erstes tue
1. Verbundene Netzwerke prüfen (`getBrandSettings`) und dir die Liste zeigen.
2. Die beste Uhrzeit je Netzwerk abfragen (`getBestTimeToPostByNetwork`).
3. Einen Testbeitrag als Entwurf oder privat anlegen und mit dir bestätigen, bevor etwas öffentlich geht.
4. Ab dann: Idee → Post (`novaaxis/social/new_post.py`) → planen (`createScheduledPost`) → berichten, was wirklich geplant ist.

## „Dauerhaft“ – was stimmt
- Die Verbindung bleibt bestehen, solange die Netzwerke den Zugriff erlauben. Meta (Instagram, Facebook), TikTok und LinkedIn lassen Zugänge nach einiger Zeit ablaufen. Metricool meldet dann „neu verbinden“. Das ist ein Klick, kein Neuaufbau.
- Der Projektstand steht in `CLAUDE.md`; jede neue Sitzung liest ihn zuerst.

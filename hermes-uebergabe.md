# Übergabe: Hermes Agent (Nous Research)

Stand: 2026-10-14. Zusammenfassung des Gesprächs. Alles basiert auf einer
Websuche und wurde **nicht** selbst installiert oder getestet. Vor der
Nutzung gegen die offizielle Doku prüfen:
https://hermes-agent.nousresearch.com/docs/getting-started/installation/

## 1. Was ist Hermes Agent?

- Open-Source-KI-Agent von Nous Research, läuft auf eigenem Rechner/Server.
- Anbindung u. a. an Telegram und Discord (laut Websuche).
- Das Sprachmodell wählt man mit `hermes model`:
  - **Cloud-API** (z. B. Nous, OpenRouter, Anthropic): wenig Hardware nötig,
    Anfragen gehen ins Internet.
  - **Lokales Modell** (z. B. über Ollama): läuft komplett lokal, braucht viel
    RAM/GPU und Speicher (mehrere GB bis über 50 GB).

## 2. Nutzen für dieses Projekt (ehrliche Einschätzung)

Das Repo enthält `business/` (Mini-AI-Aufgaben, Tracker) und
`viral_caption_tool/` (Caption-Skript). Dazu sind Claude Code und Connectors
(TikTok for Business, vidIQ, Gmail) angebunden.

- **Dafür könnte Hermes taugen:** Aufgaben, die rund um die Uhr laufen
  (z. B. Auswertungen/Erinnerungen per Telegram), ein eigener Server-Agent,
  Unabhängigkeit von Claude, andere Modelle.
- **Dagegen:** Das meiste deckt Claude Code mit den Connectors schon ab.
  Ein dauerhaft laufender Agent mit API-Keys bedeutet Sicherheits- und
  Wartungsaufwand. Mini-AI-Tasks müssen Menschen selbst erledigen; eine
  Automatisierung ist bei den Plattformen meist verboten.
- **Empfehlung:** Erst installieren, wenn es einen konkreten Bedarf gibt.

## 3. Obsidian als Gedächtnis

- Laut Community-Anleitungen möglich über einen **Filesystem-MCP-Server**:
  Hermes liest Notizen aus dem Vault und schreibt neue Notizen zurück.
- Obsidian ersetzt **nicht** das eingebaute Gedächtnis von Hermes, sondern ist
  eine zusätzliche, lesbare Ebene. (Nicht in der offiziellen Doku bestätigt.)
- Einen **eigenen Vault oder Unterordner** nur für den Agenten nutzen.
- Der Vault muss auf dem Rechner/Server von Hermes erreichbar sein
  (Sync oder Git).
- Alternative ohne Hermes: Markdown-Notizen im Repo (`CLAUDE.md`, `memory/`)
  als Gedächtnis für Claude Code.

## 4. Installation

Unterstützt: Linux, macOS, WSL2 (Android über Termux). **Native Windows wird
nicht unterstützt.** Voraussetzung: Git. Python, Node.js, ripgrep und ffmpeg
installiert das Skript selbst.

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
source ~/.bashrc
hermes model     # Anbieter wählen, API-Key eintragen
hermes doctor    # Probleme prüfen
hermes           # starten
```

Sicherheit: Das Skript erst herunterladen und lesen, bevor es ausgeführt wird.
Bei `hermes: command not found`: Shell neu laden oder `PATH` prüfen.

## 5. Installation auf Laufwerk H: (Windows)

Hermes liegt vermutlich unter `~/.hermes/`. Das ist nicht bestätigt; nach der
Installation mit `ls ~/.hermes` prüfen. Ich hatte keinen Zugriff auf H:, die
Schritte muss der Nutzer selbst ausführen.

### Option A: Ganze WSL-Distribution nach H: (empfohlen)

PowerShell als Administrator:

```powershell
wsl --install -d Ubuntu          # falls WSL noch fehlt, danach Neustart
wsl --export Ubuntu H:\ubuntu.tar
wsl --unregister Ubuntu          # erst nach erfolgreichem Export!
mkdir "H:\Agenten\WSL"
wsl --import Ubuntu "H:\Agenten\WSL" H:\ubuntu.tar
wsl -d Ubuntu
```

Danach liegt alles (auch Hermes und sein Gedächtnis) unter `H:\Agenten\WSL`.
Nach dem Import ist man evtl. `root`; bei Bedarf einen normalen Benutzer
anlegen. Dann den Befehl aus Abschnitt 4 in Ubuntu ausführen.

### Option B: Nur Hermes nach H:

In WSL:

```bash
mkdir -p /mnt/h/Agenten/hermes
ln -s /mnt/h/Agenten/hermes ~/.hermes
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

Einfacher, aber Zugriffe über `/mnt/h` sind meist langsamer. Funktioniert nur,
wenn der Installer wirklich nach `~/.hermes` schreibt.

## 6. Offene Punkte / Checkliste

- [ ] Betriebssystem klären (Windows + WSL2 laut H:-Laufwerk)
- [ ] Cloud-Modell oder lokales Modell entscheiden
- [ ] Konkreten Anwendungsfall festlegen (siehe Abschnitt 2)
- [ ] Installationspfad (`~/.hermes`) und Umgebungsvariablen in der Doku prüfen
- [ ] Bei Obsidian: Vault-Ordner für den Agenten festlegen, Sync klären
- [ ] API-Keys sicher ablegen, nicht ins Repo committen

## Quellen

- https://hermes-agent.nousresearch.com/docs/getting-started/installation/
- https://fast.io/resources/hermes-agent-installation/
- https://www.kimi.ai/resources/how-to-install-hermes-agent
- https://hermesatlas.com/use-cases/obsidian-second-brain
- https://youmind.com/landing/x-viral-articles/obsidian-hermes-agent-automation-system
- https://www.neura.market/ai-agents/resources/guides/hermes-agent-obsidian-integration-guide

# CLI-Anything (aus dem Video von @marvomatic1)

Open-Source-Projekt [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything):
baut für beliebige Software (GIMP, Blender, ComfyUI, OBS, LibreOffice …) eine
CLI, über die Claude die App direkt steuern kann – ohne MCP-Server dazwischen.

## Installation

Das Plugin ist in `.claude/settings.json` dieses Repos eingetragen und wird
in Claude Code automatisch angeboten/geladen. Manuell:

```bash
claude plugin marketplace add HKUDS/CLI-Anything
claude plugin install cli-anything@cli-anything
pip install cli-anything-hub        # Paketmanager für fertige CLIs
```

## Benutzung

In Claude Code:

```
/cli-anything <Ordner | Git-Repo-URL | App-Name>   # CLI für eine App bauen
/cli-anything:refine <app>                         # erweitern
/cli-anything:test <app>                           # Tests laufen lassen
/cli-anything:validate <app>
/cli-anything:list
```

Fertige CLIs aus dem Hub installieren:

```bash
cli-hub list            # alle verfügbaren (3D, Bild, Video, Audio, Office, KI …)
cli-hub search "video"
cli-hub install gimp    # danach: cli-anything-gimp --help
```

Hinweis: Die jeweilige Software (z. B. GIMP, Blender) muss selbst installiert
sein – die CLI ist nur die Steuerschicht dafür.

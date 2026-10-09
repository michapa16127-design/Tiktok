#!/usr/bin/env bash
# Installs the CLI-Anything package manager (cli-hub) in cloud sessions.
# The Claude Code plugin itself is enabled via .claude/settings.json.
set -euo pipefail

if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

if ! command -v cli-hub >/dev/null 2>&1; then
  pip install --quiet --root-user-action=ignore cli-anything-hub
fi

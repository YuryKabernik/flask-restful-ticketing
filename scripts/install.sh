#!/bin/sh -e

# Use the Python executable provided from the `-p` option, or a default.
[ "$1" = "-p" ] && PYTHON=$2 || PYTHON="python3"

REQUIREMENTS="requirements.txt"
VENV="venv"

set -x

"$PYTHON" -m venv "$VENV"
PIP="$VENV/bin/pip"

"$PIP" install -U pip
"$PIP" install -r "$REQUIREMENTS"

source "./$VENV/bin/activate"

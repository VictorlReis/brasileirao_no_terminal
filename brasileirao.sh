#!/bin/bash
PROJETO_DIR="$HOME/code/brasileirao_no_terminal"
if [ ! -d "$venv_name" ]; then
	python -m venv "env"
fi

source "$PROJETO_DIR/env/bin/activate"

#pip install -r requirements.txt

cd "$PROJETO_DIR"

python ~/code/brasileirao_no_terminal/main.py

deactivate

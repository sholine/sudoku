.DEFAULT_TARGET = help
.PHONY: install

## help: Display list of commands
help: Makefile
				@sed -n 's|^##||p' $< | column -t -s ':' | sed -e 's|^| |'

## install: Install prerequisite libraries
install:
				python3 -m pip install -r requirements.txt
#brew install python-tk

## version: Show wgich version of python3 is really used
version:
				which python3
				python3 -V
				python3 -m pip -V

## gen: Generates sudoku grids
gen:
				python3 "sudo generer.py"

## words: Display word version of sudoku
words:
				python3 "jeu mot-carre.py"

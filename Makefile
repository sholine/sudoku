.DEFAULT_TARGET = help
.PHONY: install

## help: Display list of commands
help: Makefile
				@sed -n 's|^##||p' $< | column -t -s ':' | sed -e 's|^| |'

## install: Install prerequisite libraries
install:
				pip install -r requirements.txt

## gen: Generates sudoku grids
gen:
				python3 "sudo generer - avec IDLE.py"

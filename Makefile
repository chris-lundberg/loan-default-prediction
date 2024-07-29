default: help

.PHONY: help
help: # Show help for each of the Makefile recipes
	@grep -E '^[a-zA-Z0-9 -]+:.*#' Makefile | sort | while read -r l; do printf "\033[1;32m$$(echo $$l | cut -f 1 -d':')\033[00m:$$(echo $$l | cut -f 2- -d'#')\n"; done

.PHONY: lint
lint: # Run linting
	docformatter *.py -r
	mypy . 
	ruff check
	yapf . --style google -d -r

.PHONY: lintable
lintable: # Run automatic formatting (eg docformatter, ruff, yapf)
	docformatter *.py -r --in-place
	ruff check --fix
	yapf . --style google -i -r
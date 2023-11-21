SHELL = cmd.exe
VENV = .venv
PYTHON = $(VENV)\Scripts\python
MYPY= $(VENV)\Scripts\mypy


default: help

.PHONY: help
help:
	



.PHONY: app/install
app/install:
	

	$(VENV)\Scripts\activate && python -m pip install --upgrade pip
	$(VENV)\Scripts\activate && python -m pip install Flask

.PHONY: app/createPY
app/createPY:
	touch src/app.py

.PHONY: app/run
app/run: 
	$(VENV)\Scripts\activate 
	setx FLASK_APP h:\CUB\ForBigData\ZpeopleWebTest\WebApplication\src\app.py
	setx FLASK_ENV development
	flask run

.PHONY: app/inEnv
app/run: 
	.venv\Scripts\activate 


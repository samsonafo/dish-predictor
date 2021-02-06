.PHONY: requirements

PROJECT_NAME = minicomp-rossman-solution
PROJECT_HOME = $(HOME)/$(PROJECT_NAME)
PYTHON_INTERPRETER = python3

test_environment:
	$(PYTHON_INTERPRETER) test_environment.py

requirements:
	$(PYTHON_INTERPRETER) -m pip install --upgrade pip
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	$(PYTHON_INTERPRETER) -m pip install -e .

dotenv:
	echo "PROJECT_NAME=$(PROJECT_NAME)" > .env
	echo "PROJECT_HOME=$(PROJECT_HOME)" >> .env

init:
	mkdir -p $(PROJECT_HOME)/data/raw
	mkdir -p $(PROJECT_HOME)/data/interim
	mkdir -p $(PROJECT_HOME)/data/processed
	mkdir -p $(PROJECT_HOME)/models
	mkdir -p $(PROJECT_HOME)/reports

lint:
	flake8 src

clean_up:
	find . -type f -name "*.py[co]" -delete
	find . -type f -name "*.ipynb_checkpoints" -delete
	find . -type d -name "__pycache__" -delete

# ROSSMAN PROJECT SPECIFIC

make rossman: init
	rm -rf minicomp-rossman
	git clone https://github.com/ADGEfficiency/minicomp-rossman
	cd minicomp-rossman; $(PYTHON_INTERPRETER) data.py --test 1
	mv minicomp-rossman/data/*.csv $(HOME)/$(PROJECT_NAME)/data/raw


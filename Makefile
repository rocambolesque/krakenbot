init:
	virtualenv venv -p python3.5
	venv/bin/pip install -r requirements.txt

init-dev: init
	venv/bin/pip install -r requirements-dev.txt

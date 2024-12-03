all:
	python3.11 -m venv venv && \
	source venv/bin/activate && \
	pip install -r requirements.txt && \
	flask run

env:
	set FLASK_APP=app.py

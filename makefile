all:
	pip freeze > requirements.txt
	flask run

env:
	set FLASK_APP=app.py

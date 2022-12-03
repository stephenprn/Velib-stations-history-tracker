test:
	pytest

venv:
	source env/bin/activate

freeze:
	env/bin/python -m pip freeze > requirements.txt


server:
	flask run --host 0.0.0.0 -p 5000

compose:
	docker-compose up -d

format:
	black app && autopep8 --in-place --aggressive --aggressive --recursive ./app
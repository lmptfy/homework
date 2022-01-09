install:
	pipenv install

shell:
	pipenv shell

run:
	pipenv run uvicorn main:app --reload

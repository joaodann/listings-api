run:
	@echo Running server at localhost:8000
	env/bin/python3 manage.py runserver
test:
	@echo Preparing to run tests
	env/bin/python3 manage.py test listings_api -k
migrate:
	@echo Creating necessary migrations...
	env/bin/python3 manage.py makemigrations
	@echo Applying migrations...
	env/bin/python3 manage.py migrate
shell:
	@echo Opening Django shell...
	env/bin/python3 manage.py shell
updaterequirements:
	@echo Update requirements...
	env/bin/pip3 install -r requirements.txt
black:
	@echo run black...
	env/bin/black listingsapi --line-length 79
flake8:
	@echo run flake8...
	env/bin/flake8 listingsapi
deploy:
	git push heroku master
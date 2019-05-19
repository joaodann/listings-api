run:
	@echo Running server at localhost:8000
	env/bin/python3 listingsapi/manage.py runserver
test:
	@echo Preparing to run tests
	env/bin/python3 listingsapi/manage.py test listings_api
migrate:
	@echo Creating necessary migrations...
	env/bin/python3 listingsapi/manage.py makemigrations
	@echo Applying migrations...
	env/bin/python3 listingsapi/manage.py migrate
shell:
	@echo Opening Django shell...
	env/bin/python3 listingsapi/manage.py shell
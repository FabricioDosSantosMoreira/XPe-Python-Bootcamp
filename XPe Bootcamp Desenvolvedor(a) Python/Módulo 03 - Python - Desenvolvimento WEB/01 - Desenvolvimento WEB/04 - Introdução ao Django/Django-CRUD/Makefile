.PHONY: run-all run run-migrate run-coverage create-superuser

run-all:
	make run-migrate && make create-superuser && make run

run:
	cd .\project\ && python manage.py runserver

run-migrate:
	cd .\project\ && python manage.py makemigrations application && python manage.py migrate

run-coverage:
	cd .\project\ && coverage run manage.py test && coverage report && coverage html

create-superuser:
	cd .\project\ && python manage.py createsuperuser

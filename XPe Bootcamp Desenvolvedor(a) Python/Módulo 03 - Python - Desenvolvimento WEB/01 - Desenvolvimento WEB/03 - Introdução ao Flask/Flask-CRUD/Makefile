.PHONY: run

run:
	@set FLASK_APP=project.app:get_app && flask run

run-migrate:
	@set FLASK_APP=project.app:get_app && flask db init && flask db migrate && flask db upgrade

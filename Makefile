MAKE_FILE_SETTING := settings

migrations:
	python3.6 manage.py makemigrations core place users items

migrate:
	python3.6 manage.py migrate

runserver:
	python3.6 manage.py runserver 0.0.0.0:8000

test:
	python3.6 manage.py test refrigerator_manager.apps.items.tests.test__items_api

#coverage:
 #   coverage report
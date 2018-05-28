MAKE_FILE_SETTING := settings

migrations:
	python3.6 manage.py makemigrations core place users items

migrate:
	python3.6 manage.py migrate

runserver:
    python3.6 manage.py runserver 0.0.0.0:8000


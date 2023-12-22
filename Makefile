dev:
	poetry run python3 manage.py runserver
	
makemessages:
	poetry run django-admin makemessages -l ru
	
compilemessages:
	poetry run django-admin compilemessages
# recipe-app-api

```bash
docker-compose run recipe_app sh -c "python manage.py startapp app"
docker-compose run recipe_app sh -c "python manage.py startapp core"
docker-compose run recipe_app sh -c "python manage.py test & flake8"
docker-compose run recipe_app sh -c "python manage.py makemigrations"
```


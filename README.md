# Bookstore

Bookstore APP from Backend Python course from EBAC

## Prerequisites

```
Python 3.8+
Poetry (optional)
Docker & docker-compose (optional)
```

## Quickstart

1. Clone this project

   ```shell
   git clone git@github.com:GabrielPintoDev/bookstore.git
   cd bookstore
   ```

2. Using Poetry (recommended)

   ```shell
   poetry install
   poetry run python manage.py migrate
   poetry run python manage.py createsuperuser
   poetry run python manage.py runserver
   ```

3. Using virtualenv + pip (alternative)

   ```powershell
   python -m venv env
   .\env\Scripts\Activate.ps1   # PowerShell on Windows
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

4. Docker (development)

   ```shell
   docker-compose up -d --build
   docker-compose exec web python manage.py migrate
   ```

   Replace `web` with your service name if different.

5. Run tests

   ```shell
   pytest
   # or inside docker
   docker-compose exec web python manage.py test
   ```

6. Lint and format

   ```shell
   flake8 .
   black .
   ```

7. Collect static files (production)

   ```shell
   python manage.py collectstatic --noinput
   ```

8. Stop and remove Docker containers

   ```shell
   docker-compose down
   ```

If you want, I can adjust these steps for Windows CMD, WSL, or add examples for running the app with `poetry shell`.

URLs:

https://gabrielandradepinto.pythonanywhere.com/bookstore/v1/product/
https://gabrielandradepinto.pythonanywhere.com/bookstore/v1/order/
https://gabrielandradepinto.pythonanywhere.com/bookstore/v2/product/
https://gabrielandradepinto.pythonanywhere.com/bookstore/v2/order/
https://gabrielandradepinto.pythonanywhere.com/hello/
https://gabrielandradepinto.pythonanywhere.com/admin/login/?next=/admin/
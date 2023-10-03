# testAdmin
Create venv
> python -m venv venv
Activate it
> \venv\Scripts\activate
Update pip and download requirements
> pip install --upgrade pip
> pip install -r requirements-dev.txt
Make db migration
> flask db init
> flask db migrate
> flask db upgrade

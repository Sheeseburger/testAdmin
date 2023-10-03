# testAdmin
Create venv
> python -m venv venv

Activate it
> \venv\Scripts\activate

Update pip and download requirements
> pip install --upgrade pip

> pip install -r requirements-dev.txt

Make db migration. Can be skipped, if DB uri wasn't changed.
> flask db init
> flask db migrate
> flask db upgrade
For adding test data set CREATE_DEFAULT_DATA=True in .flaskenv.
Run flask
> flask run

Login route is '/login'. Login accept username and password. In DB there is only {username:admin, password:admin}. Products route is '/'. 

> GET returns all products. Can be added Three queries offer_of_the_month, available, self_pickup True or False each.

>POST needs next fields name, photo_url, category, description,price. Offer_of_the_month,available, self_pickup default values is True. Price is int 

> PATCH request structure is {"id":x, "data": {...}}, where data is fields to be updated
 
> DELETE request structure is {"id":x}. 

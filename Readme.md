# Django & Django REST framework test project.
The test project won't be used in any real environment.


## Summary:

Django REST Framework for a simple prebuild booking app that have:
- Listing object 
- Filtering through Listings and returning JSON response with available units based on search criterias.
- Handle large dataset of Listings.

- Database is prefilled with information - **db.sqlite3**.
    - superuser
        - username: **admin**
        - password: **admin**


## Project setup
    git clone https://github.com/Ysnz/bookingengine.git
    python -m venv venv
    pip install -r requirements.txt
    python manage.py runserver

PS: Don't forget to add .env file.



## Request example:

http://localhost:8000/api/v1/available/?max_price=100&check_in=2021-12-09&check_out=2021-12-12


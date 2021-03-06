# ProductFolio

### Concept

Open source, small e-commerce.

### Tech

Python3/Django3, Bootstrap4.

### License

ProductFolio is licensed under the **MIT License**.

### Credits

Colorlib: https://colorlib.com

### Development

1. Clone The Repository:

    ```
    git clone https://github.com/alnuaimi94/ProductFolio
    ```

2. Change Directory:

    ```
    cd ProductFolio
    ````

3. Create Virtualenv & Active it:

    ```
    python -m venv venv & venv\Scripts\activate
    ```

4. Install PIP Requirements:

    ```
    pip install -r requirements-dev.txt
    ```

5. Set DJANGO_CONFIGURATION as a 'Local' instead of 'Production' in asgi.py, wsgi.py and manage.py files

6. Create .env file in the root of the project and set:
    ```
    SECRET_KEY=somethingHere
    ADMIN_URL=somethingHere/
    ```

7. Migrate & Createsuperuser:

    ```
    python manage.py migrate & python manage.py createsuperuser
    ```

8. Collectstatic & Runserver:

    ```
    python manage.py collectstatic & python manage.py runserver
    ````

### Screenshots

#### Home Page

![alt text](https://github.com/alnuaimi94/ProductFolio/blob/master/_screenshots/home.png)

#### Detail Page

![alt text](https://github.com/alnuaimi94/ProductFolio/blob/master/_screenshots/detail1.png)

#### About Page

![alt text](https://github.com/alnuaimi94/ProductFolio/blob/master/_screenshots/about.png)

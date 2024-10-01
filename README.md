Django E-commerce Platform

This is a Django-powered e-commerce platform for managing categories, products, customers, orders, and a shopping cart system. It supports user authentication, cart management, and order processing. The project is designed using Django Rest Framework (DRF) and includes API endpoints for interacting with the system.
Features

    User Registration and Authentication (Login, Logout, Signup)
    Product Listing and Details
    Shopping Cart Management
    Order Management
    Status Tracking for Orders
    API built with Django Rest Framework (DRF)

Tech Stack

    Backend: Django, Django Rest Framework
    Database: SQLite (default), PostgreSQL, or any other compatible Django database
    Frontend: Css, Html, Bootstrap
    Authentication: Token-based authentication using djangorestframework-simplejwt or similar package

Installation

    Clone the repository:

    bash git clone https://github.com/Alirezaalireza77/e-commerce.git
         



Create and activate a virtual environment:

    bash python -m venv venv
         source venv/bin/activate  # On Windows use `venv\Scripts\activate`



Install the required dependencies:

    bash pip install -r requirements.txt



Set up the database:

    bash python manage.py migrate



Create a superuser to access the admin panel:

    bash python manage.py createsuperuser



Run the development server:

    bash python manage.py runserver

    

Environment Variables

To run this project, you need to set the following environment variables. Create a .env file in the root directory with these variables:

    bash SECRET_KEY='django-insecure-4f_x9@r$qn$kv0bgx$3+e$jdshf14za657hzc0_$9kiz#z9)&u'
         DEBUG=True
         DATABASE_URL='127.0.0.1:5432'



API Documentation

The API endpoints are built using Django Rest Framework. To explore the available endpoints, run the server and visit the DRF Browsable API at:



http://127.0.0.1:8000/shop/

Running Tests

To run the tests:

    bash python manage.py test



Tests are written using Django's TestCase and APITestCase along with Factory Boy for fixtures.


Contributions are welcome! Please open a pull request or an issue for any suggestions or bug reports.


This project is licensed under the MIT License. See the LICENSE file for details.


For any queries, please contact:

    Alireza
    GitHub: Alirezaalireza77

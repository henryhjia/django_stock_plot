# Stock Price Viewer Django Version
## Project Overview

**Stock Price Viewer** is a **Django** based web application designed to fetch and visualize historical stock prices from **Yahoo Finance.**
The application is developed **with the help of AI-assisted programming using Gemini-pro-2.5,** which helped streamline the coding process and improve efficiency.

Given the following **required fields:**

- Stock Ticker
- Start Date
- End Date

The app will:

- Retrieve historical stock prices for the specified date range from Yahoo Finance.
- Generate a plot of stock price versus date for easy visualization.
- Display the most recent stock price, covering up to the last 20 days.

## Project Structure
```
    1 /home/henryjia/Projects/django_stock_plot/
    2 ├── stock_project/            # The main Django project directory
    3 │   ├── stock_project/        # Core project configuration
    4 │   │   ├── __init__.py
    5 │   │   ├── settings.py       # Project settings (apps, database, etc.)
    6 │   │   ├── urls.py           # Project-level URL routing
    7 │   │   ├── wsgi.py           # Web server gateway interface
    8 │   │   └── asgi.py           # Asynchronous server gateway interface
    9 │   ├── stock_plot/             # Your application
   10 │   │   ├── __init__.py
   11 │   │   ├── admin.py          # Admin site configuration
   12 │   │   ├── apps.py           # App configuration
   13 │   │   ├── migrations/       # Database migration scripts
   14 │   │   ├── models.py         # Database models (we haven't used this yet)
   15 │   │   ├── templates/        # HTML templates
   16 │   │   │   └── stock_plot/
   17 │   │   │       └── index.html  # Your UI template
   18 │   │   ├── app_tests/          # Your unit tests
   19 │   │   │   ├── __init__.py
   20 │   │   │   └── test_views.py # Tests for your views
   21 │   │   ├── urls.py           # App-level URL routing
   22 │   │   └── views.py          # **<-- YOUR CORE LOGIC IS HERE**
   23 │   ├── manage.py             # Command-line utility for project management
   24 │   └── db.sqlite3            # Your SQLite database file
   25 └── venv/                     # Your Python virtual environment

```

## Running the Application Locally
  1. Activate the virtual environment 
  ```
  source .venv/bin/activate
  ```
  2. Start the Django application
  ```
  cd stock_project/
  python manage.py runserver
  ```
  3. Open the app in your browser
  Visit http://127.0.0.1:8000/stock_plot to access **Stock Price Viewer**


## Unit Test in local enrionment
```
  cd stock_project
  python manage.py test
```
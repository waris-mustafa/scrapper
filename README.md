# Scrapper

Scrapper is a Django application that works on the basic authentication of a user and allowing him/her to be able to scrape a website for emails.

## Description

This project is a Django application. It includes the following features:
- Feature 1: User authentication and authorization as well as Admin Control
- Feature 2: Scraping Emails from a URL
- Feature 3: Sending Email to the scraped Emails

## Installation

1. Install Poetry if you haven't already:
    ```bash
    curl -sSL https://install.python-poetry.org | python3 -
    ```

2. Install the dependencies:
    ```bash
    poetry install
    ```

3. Apply the migrations:
    ```bash
    poetry run python manage.py migrate
    ```

4. Run the development server:
    ```bash
    poetry run python manage.py runserver
    ```

## Usage

1. Start the development server:
    ```bash
    poetry run python manage.py runserver
    ```

2. Open your web browser and go to `http://127.0.0.1:8000/`.

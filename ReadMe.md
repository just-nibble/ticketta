# Tickeeta API

An API service for the creation and management of events as well as the sale and puchase of tickets

## Description

This API allows you to create multiple events and tickets, you can view purchases made for tickets

## Getting Started

### Dependencies

- Python 3.6 and above
- Refer to the requirements.txt file

### Installing
1. Build the container by running ``` docker build ticketta:v1 . ```
2. Run the container by running ```docker run --env-file=.env -p 8000:8000 ticketta:v1 ```

## Alternatively ##
1. RUN ```pip install -r requirements.txt```
- A running virtual environment is advised

2. run ```python manage.py migrate```
3. run ```python manage.py runserver```

### Usage ###
Documentation is available at /docs
# LittleLemon
This is the capstone project for the Coursera course Meta Back-End Developer Professional Certificate.


# The API endpoints implemented
## Basic functionalities
### API home for static asset serving
You can check it out in the browser.
    api/
### All menu items
    api/menu/
    api/menu-items/
User must log in in order to access it.
It accepts the following request types:
* GET
* POST

### Specific menu items
    api/menu/<int:pk>
    api/menu-items/<int:pk>
User must log in in order to access it.
It accepts the following request types:
* GET
* PUT
* PATCH
* DELETE

### Bookings
    api/booking/tables/
    restaurant/booking/tables/
User must log in in order to access it.
It accepts the following request types:
* GET
* POST

## Authentication
### Get token for the user
    api/api-token-auth/
    auth/token/login/
It accepts only the following request type:
* POST
### Destroy user token
    auth/token/logout/
It accepts only the following request type:
* POST

## Installation and troubleshooting
I've used Pipenv for virtual environment management, because it requires less space to store.
In order to make it work, please go to the directory where the **```Pipfile```** is located. Run the following commands in the terminal:

    pipenv shell
    pipenv install

In case there is no python 3.10 installed on your computer, please amend the following line in **```Pipfile```**:

    [requires]
    python_version = "3.10"

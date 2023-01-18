# Django meetup - Django and Scrapy elegant way to crawl and store data

## Installation

The following guide assumes installation on Ubuntu 18.04+ or similar Debian based GNU/Linux distribution.

### System Requirements

##### Base

* Ubuntu 18.04+ or similar
* Python 3.6+
* Django 3.0+

#### Application

Install requirements:

    $ pip install -r requirements.txt

Run database migrations:

    $ python manage.py migrate

Run development server:

    $ python manage.py runserver

Craw dnevnik with scrapy:

    $ cd dnevnik
    $ scrapy crawl dnevnik

Craw dnevnik with django command:

    $ python manage.py crawl
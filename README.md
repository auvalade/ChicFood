**Chic**Food
============

**So, I like food. **

This little website is a food showcase, on which you can add all your favorite food and display it on a nice frontpage.

*Some features: *

-   Elastic Search Powered

-   Login to add your own food !

-   Nice Materialize Responsive Design


1 – The setup
-------------

You need:

-   Python 3.4 (3.5+ should work too)

-   Django 1.9 (1.8+ should work too)

-   A PostgreSQL database installed, to set in helloseechic/settings.py at DATABASES (don’t forget to migrate all once done)

-   An ElasticSearch server running, to set in helloseechic/settings.py at ES\_CLIENT


2 – How to use
--------------

Once everything is up and running, the rest is pretty straightforward. All you need is a user on your database (the fastest way is to make a superuser with the ‘python3 manage.py createsuperuser’ command).

After that, just open the main page, login and start adding some tasty food !

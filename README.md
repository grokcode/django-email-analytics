Django Email Analytics
====

Django Email Analytics adds Google Analytics tracking to emails sent with Django. It provides a wrapper for Django's standard email backends.

Installation and Setup
----

Install with pip:

    pip install django-email-analytics

Then set the email backend in the settings.py file.

    EMAIL_BACKEND = 'emailanalytics.backends.AnalyticsEmailBackend'

Set `EMAIL_ANALYTICS_BACKEND` to the value you previously used for `EMAIL_BACKEND`. Or if `EMAIL_BACKEND` was unset, you can leave `EMAIL_ANALYTICS_BACKEND` unset as well. This will chain the email backends so that django-email-analytics will use your original backend to send messages. 
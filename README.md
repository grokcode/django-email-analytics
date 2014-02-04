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

Options
----

By default, URLs will be replaced only when the mimetype is text/html and the URL occurs within a `href` attribute.

Set `EMAIL_ANALYTICS_REPLACE_TXT` to `True` if you would like to also replace urls occuring in text emails.


Tracking details
----

If a URL already contains tracking parameters, they are left unchanged.

Otherwise, URLs are tagged with the following parameters:

* `utm_source` is set to the subject of the email
* `utm_medium` is set to `email`
* `utm_campaign` is set to `webapp`

See here for a [description of the tracking parameters](https://support.google.com/analytics/answer/1033867?rd=2).

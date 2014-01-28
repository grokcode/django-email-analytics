try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'django-email-analytics',
    'version': '0.1',
    'author': 'Jess Johnson',
    'author_email': 'jess@grokcode.com',
    'packages': ['emailanalytics'],
    'scripts': [],
    'url': 'http://pypi.python.org/pypi/django-email-analytics/',
    'license': 'LICENSE.txt',
    'description': 'Adds Google Analytics tracking to emails sent with Django.',
    'long_description': open('README.txt').read(),
    'install_requires': [],
}

setup(**config)

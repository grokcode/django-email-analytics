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
    'url': 'https://github.com/grokcode/django-email-analytics',
    'license': 'LICENSE.txt',
    'description': 'Adds Google Analytics tracking to emails sent with Django.',
    'long_description': open('docs/README.rst').read(),
    'install_requires': ['beautifulsoup4'],
}

setup(**config)

from setuptools import setup

setup(
    name='python-google-calendar-parser',
    version='0.0.0',
    py_modules=['google_calendar_parser'],
    install_requires=[
        'pytz',
        'beautifulsoup4',
        'icalendar',
        'python-dateutil',
        'six',
    ],
)

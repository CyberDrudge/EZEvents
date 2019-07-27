from setuptools import setup
from os import path

DIR = path.dirname(path.abspath(__file__))
INSTALL_PACKAGES = ['google-api-python-client', 'google-auth-httplib2', 'google-auth-oauthlib']

with open(path.join(DIR, 'README.md')) as f:
    README = f.read()

setup(
    name='ezevents',
    packages=['ezevents'],
    description="View your upcoming events and add events to your Google Calendar",
    long_description=README,
    long_description_content_type='text/markdown',
    install_requires=INSTALL_PACKAGES,
    entry_points={
        'console_scripts': ['ezevents=ezevents.ezevents:main'],
    },
    include_package_data=True,
    version='0.3',
    url='http://github.com/CyberDrudge/EZEvents',
    author='Satyam Saxena',
    author_email='cyberdrudge77@gmail.com',
    keywords=['calendar', 'python', 'events'],
    python_requires='>=2.6'
)
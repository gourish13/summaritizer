"""
Environment Vars
"""

from os import environ

EMAIL_ID, EMAIL_PWD = environ['EMAIL'].split()

BASE_URL = environ['BASE_URL']

DATABASE_URL = environ['DBURI']

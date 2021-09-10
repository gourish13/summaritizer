"""
Database Connection
"""

from app.consts.envs import DATABASE_URL

from pydal import DAL

db = DAL(DATABASE_URL, pool_size=4, lazy_tables=True)

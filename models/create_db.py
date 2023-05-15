# from flask_sqlalchemy import SQLAlchemy
from peewee import MySQLDatabase, Model
from os import getenv
import logging as log

try:
    USERNAME = getenv('DB_USERNAME') or 'root'
    PASSWORD = getenv('DB_PASSWORD') or ''
    DATABASE = getenv('DB_DATABASE') or 'laporbarang'
    SERVER   = getenv('DB_SERVER')   or 'localhost'
    PORT     = getenv('DB_PORT') or 3306
    db = MySQLDatabase(
        database=DATABASE,
        user=USERNAME, 
        password=PASSWORD,
        host=SERVER, 
        port=int(PORT)
        )
    class BaseModel(Model): 
        """A base model that will use our MySQL database"""
        class Meta:
            database = db

except Exception as e:
    log.error('Error while setup database: ')
    log.error(e)
import os


class Config(object):
    """ Main configuration variables """

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MONGO_URI = os.environ.get('MONGO_URI')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME')

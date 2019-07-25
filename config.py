import os


class Config(object):
    """ Main configuration variables """

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'change-this'
    MONGO_URI = 'mongodb+srv://antAdmin:dbfirstAdmin@mf-cluster-01-fnb1e.mongodb.net/mf-db-01?retryWrites=true&w=majority'
    MONGO_DBNAME = 'mf-db-01'


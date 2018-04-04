import os


class BaseConfig:

    PROJECT = 'volt'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False


    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = 'secret key'

    LOG_FOLDER = '/tmp/volt/logs'

    # Fild upload, should override in production.
    # Limited the maximum allowed payload to 16 megabytes.
    # http://flask.pocoo.org/docs/patterns/fileuploads/#improving-uploads
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    UPLOAD_FOLDER = '/tmp/uploads'


class DefaultConfig(BaseConfig):

    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_DATABASE_URI = 'postgresql://scott@localhost/trading'
    SQLALCHEMY_DATABASE_URI = 'postgresql://billy@localhost/testdb'
    SQLALCHEMY_BINDS = {
        'cruncher': 'postgresql://emhtadmin:emhtadmin@localhost:32769/emht'
    }


class TestConfig(BaseConfig):

    TESTING = True
    CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://billy@localhost/testdb'

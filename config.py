import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'cut-the-bs'
	SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:myPassword@localhost/blogger'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

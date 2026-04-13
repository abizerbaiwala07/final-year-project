import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess-this-super-secret-key'
    
    # SQLite for dev, can be overridden by DATABASE_URL environment variable for prod (PostgreSQL)
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # ML Model Path
    MODEL_PATH = os.path.join(basedir, 'app', 'ml', 'model.pkl')

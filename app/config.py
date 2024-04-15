import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'kyle'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://kylebessemer@localhost:5432/users_orders'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

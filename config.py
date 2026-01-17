"""
Configuration settings for the application
"""
import os
from datetime import timedelta

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://localhost/taskdb')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

import os


class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql:///tastebuds"
    SQLALCHEMY_TRACK_MODIFICATION = False
    JWT_SECRET_KEY = 'cat_blat'
    JWT_TOKEN_LOCATION = ['query_string', 'headers']

"""
    Apache License 2.0 Copyright (c) 2023 Pavel Bystrov
    Flask web-app configuration
"""
import logging
import os
from datetime import timedelta


basedir = os.path.abspath(os.path.dirname(__file__))
logging.basicConfig(filename='webapp.log', level=logging.INFO)
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir,
                                                      "..",
                                                      "webapp.db")
SECRET_KEY = "ASDWQYUhj342678gvmjhxckbdvkjbscde"
REMEMBER_COOKIE_DURATION = timedelta(days=15)
SQLALCHEMY_TRACK_MODIFICATIONS = True

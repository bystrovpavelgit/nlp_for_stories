"""
    Apache License 2.0 Copyright (c) 2023 Pavel Bystrov
    business logic for dish recommendations
"""
import logging
from sqlite3 import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from webapp.user.models import User


def get_user_by_name(name):
    """  get user by name """
    try:
        user = User.query.filter_by(username=name).first()
        return user
    except (SQLAlchemyError, IntegrityError) as exc:
        error = str(exc.__dict__["orig"])
        msg = f"Exception {error} in get_user_by_name({name}) "
        logging.error(msg)
        return None

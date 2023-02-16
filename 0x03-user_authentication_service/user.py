#!/usr/bin/env python3
""" script to define the database schema for this project """


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence

Base = declarative_base()


class User(Base):
    """ Base class for the User model """
    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)

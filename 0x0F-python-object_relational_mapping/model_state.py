#!/usr/bin/python3
"""Definition of class states"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """defines state class
    Attributes:
    id(int): state id
    name(str): name of the state
    __tablename__(str): table name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    name = Column(String(128), nullable=False)

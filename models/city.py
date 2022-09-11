#!/usr/bin/python3
"""This is the city class"""
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """This is the class for City
    Attributes:
        state_id: The state id
        name: input name
        __tablename__: SQL table
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey(State.id), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities")

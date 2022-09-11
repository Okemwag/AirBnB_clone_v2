#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    __tablename__: SQL table
    cities: for DBStorage, creates relationship for class City to state table
    """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """ Getter for cities with same state_id
            """
            r_v = []
            objs = models.storage.all()
            for key, value in objs.items():
                if key.split(".")[0] == "City":
                    if self.id == value.state_id:
                        r_v.append(value)
            return (r_v)

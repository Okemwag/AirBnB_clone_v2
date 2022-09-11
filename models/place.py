#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from models.user import User
from models.amenity import Amenity
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
from sqlalchemy import *


""" TO-DO:
     amenities setter needs to be coded
     check amenities class attribute if backref correct
     place_amenity instance for Many-to-Many table
"""


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
        reviews: relationship class attribute to Review
        amenities: relationship class attribute to Amenity
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey(City.id), nullable=False)
    user_id = Column(String(60), ForeignKey(User.id), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place")
    amenities = relationship("Amenity", backref="place_amenities",
                             secondary=place_amenity, viewonly=False)
    amenity_ids = []

    @property
    def amenities(self):
        """ Getter
        """
        return self.amenity_ids

    @amenities.setter
    def amenities(self, v):
        """ Setter
        """
        if isinstance(v, Amenity):
            self.amenity_ids.append(v.id)

    @property
    def reviews(self):
        """ Getter
        """
        r_v = []
        objs = storage.all()
        for key in objs.keys():
            if key.split(".")[0] == "Review":
                if key.split(".")[1] == self.id:
                    r_v.append(objs[key])

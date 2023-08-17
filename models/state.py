#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Getter"""
            from models import storage
            from models.city import City
            all_cities = []
            for city_obj in storage.all(City).values():
                # key = key.split(".")[0]
                # if key == "City" and city_obj.state_id == self.id:
                if city_obj.state_id == self.id:
                    all_cities.append(city_obj)
            return all_cities

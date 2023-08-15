#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Getter"""
            all_cities = []
            for key, value in self.all().items():
                key = key.split(".")
                if key == 'City' and value.state_id == self.id:
                    all_cities.append(value)
            return all_cities

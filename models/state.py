#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')


@property
def cities(self):
    """Getter"""
    all_cities = []
    for key, value in self.all().items():
        key = key.split(".")
        if key == 'City' and value.state_id == self.id:
            all_cities.append(value)
    return all_cities

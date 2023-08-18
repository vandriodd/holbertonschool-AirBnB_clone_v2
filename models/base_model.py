#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instantiates a new model"""
        if kwargs:
            kwargs.pop("__class__", None)
            for k, v in kwargs.items():
                if k == "updated_at" or k == "created_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, k, v)
            if not self.__dict__.get("created_at"):
                self.created_at = datetime.now()
                self.updated_at = self.created_at
            if not self.id:
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        instance_dict = {k: v for k, v in self.__dict__.items()}
        instance_dict.pop("_sa_instance_state", None)
        return '[{}] ({}) {}'.format(cls, self.id, instance_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.pop("_sa_instance_state", None)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        """ Delete the current instance from the storage """
        from models import storage
        return storage.delete(self)

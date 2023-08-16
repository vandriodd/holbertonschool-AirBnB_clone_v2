#!/usr/bin/python3
"""
db_storage module
Contains DBStorage class that handles db interactions using SQLAlchemy
"""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy.orm import scoped_session, sessionmaker
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """Class that handles db interactions"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes an instance of DBStorage class"""
        # Retrieves db credentials and config from env vars
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        # Create SQAlchemy engine
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)

        # If testing, all db tables are dropped
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return all objects of a class"""
        dictionary = {}
        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            for instance in self.__session.query(cls).all():
                key = f"{instance.__class__.__name__}.{instance.id}"
                dictionary[key] = instance
        else:
            for obj in classes:
                for instance in self.__session.query(obj).all():
                    key = f"{instance.__class__.__name__}.{instance.id}"
                    dictionary[key] = instance
        return dictionary

    def new(self, obj):
        """Add obj to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the db and establishes session"""
        # Create all tables in the db using provided engine
        Base.metadata.create_all(self.__engine)
        # Create sessions linked to db engine
        db_sessions = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Create a scoped session from db_sessions and assign
        Session = scoped_session(db_sessions)
        self.__session = Session

    def close(self):
        """Closes the active session"""
        self.__session.remove()

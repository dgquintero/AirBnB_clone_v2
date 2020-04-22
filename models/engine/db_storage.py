#!/usr/bin/python3
"""This is the DB storage class for AirBnB"""
import json
from os import getenv
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


all_classes = {"Amenity": Amenity, "State": State, "City": City, "User": User,
               "Place": Place, "Review": Review}


class DBStorage:
    """ DBStorage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """ DBStorage engine
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv("HBNB_MYSQL_USER"),
            getenv("HBNB_MYSQL_PWD"),
            getenv("HBNB_MYSQL_HOST"),
            getenv("HBNB_MYSQL_DB")), pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all function to query on the current database session
        """
        instance = {}
        for classes in all_classes:
            if cls is None or cls is all_classes[classes] or cls is classes:
                objs = self.__session.query(all_classes[classes]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    instance[key] = obj
        return (instance)

    def new(self, obj):
        '''
        Create a new obj
        '''
        self.__session.add(obj)

    def save(self):
        '''
        commit changes
        '''
        self.__session.commit()

    def delete(self, obj=None):
        '''
        Delete an obj
        '''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''
        Reload all obj
        '''
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False, )
        session = scoped_session(Session)
        self.__session = session

    def close(self):
        """
        public method that calls remove method
        """
        self.__session.close()

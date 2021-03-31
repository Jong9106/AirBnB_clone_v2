#!/usr/bin/python3

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


class Dbstorage():
    """ New Class to manage and store hbnb in MySQL """

    __engine = None
    _session = None

    def __init__(self):
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBN_MYSQL_DB')
        HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')

        self.engine = create_engine('mysql+mysqldb://{}:{}@{}host/{}'
                       .format(HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB),
                       pool_pre_ping=True)

        Base.metadata.create_all(engine)

        Session = sessionmaker(engine)
        session = Session()
    
    def all(self, cls=None):
        self.__session = 
        if cls is not None:
            new_dic = {}
            for key,value in self.__objects.items():
                if cls == value.__class__:
                    new_dic[key] = value
            return new_dic

    def new(self, obj):
        self.__session.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})
    def save(self): 
        self.__session
    def delete(self, obj=None)

    def reload(self):
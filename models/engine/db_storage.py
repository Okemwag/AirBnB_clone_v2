#!/usr/bin/python3
"""This is the DBStorage class for AirBnB"""

from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from os import getenv, environ
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session


classes = {"City": City,
           "State": State,
           "Place": Place,
           "User": User,
           "Review": Review,
           "Amenity": Amenity}


class DBStorage:
    """This class handles the MySQL database engine
    Attributes:
        __engine: initially set to None, becomes sqlalchemy engine
        __session: initially set to None, becomes sqlalchemy session
    """

    __engine = None
    __session = None

    def __init__(self):
        """ Instantiation of DBStorage class
        Attributes:
        engine: links to MySQL database using environment variables
        """
        DBStorage.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                           .format(getenv('HBNB_MYSQL_USER'),
                                                   getenv('HBNB_MYSQL_PWD'),
                                                   getenv('HBNB_MYSQL_HOST'),
                                                   getenv('HBNB_MYSQL_DB')),
                                           pool_pre_ping=True)
        self.reload()

        if getenv('HBNB_ENV') == "test" and 'test' in os.environ:
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Queries current database session for class objects
        If class not specified, queries all types of objects
        """
        return_dic = {}
        query = []
        for key in classes.keys():
            query = DBStorage.__session.query(classes[key]).all()
            for obj in query:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                return_dic[key] = obj
        return return_dic

    def new(self, obj):
        """add the object to the current database session
        """
        if obj:
            DBStorage.__session.add(obj)

    def save(self):
        """ commits all changes of the current database session
        """
        DBStorage.__session.commit()

    def delete(self, obj=None):
        """ deletes from the current database session obj if not None
        """
        if obj:
            DBStorage.__session.delete(obj)

    def reload(self):
        """creates all tables in the database
        creates the current database session (self.__session)
        from the engine (self.__engine)
        """
        Base.metadata.create_all(DBStorage.__engine)
        session_make = sessionmaker(bind=DBStorage.__engine,
                                    expire_on_commit=False)
        session_scoped = scoped_session(session_make)
        DBStorage.__session = session_scoped()

    def close(self):
        """close session
        """
        DBStorage.__session.close()

import os
import sys
# this is for the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# we will use it in the configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# this in order to create our Foreign key relationships, also we'll use it
# to write our mapper
from sqlalchemy.orm import relationship

# we will use in the configuration code at the end of the file
from sqlalchemy import create_engine

# instance of declarative_base() the classes are special alchemy classes
# that correspond to tables in the database
Base = declarative_base()


class Restaurant(Base):  # B
    __tablename__ = 'restaurant'  # A

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))  # A ref to table.column
    # just a variable which i'm saying is the relationship between my class restaurant
    restaurant = relationship(Restaurant)  # B reference to class

# We added this serialize function to be able to send JSON objects in a
# serializable format
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'course': self.course,
        }
# ------------insert at end of file------------------------

# create an instance of create_engine and point to the db we'll use


engine = create_engine('sqlite:///restaurantmenu.db')
# this goes in to the database and add the classes we will soon create as new
# tables in the database
Base.metadata.create_all(engine)

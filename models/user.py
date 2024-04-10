from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__= "users"
#validations within the table
    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable= False)
    email = Column(String(120), unique= True, nullable= False)

#For object creation
    def __init__(self, username,email):
        pass

#representation of the string
    def __repr__(self):
        return f"User {self.username}"

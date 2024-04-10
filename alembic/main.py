#create db using engine in the connection string
from sqlalchemy import create_engine
#it avails the session object to run query methods on my db
from sqlalchemy.orm import sessionmaker
from models.user import User
from models.base import Base

#creating the db
DATABASE_URI = "sqlite:///persons.db"
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

#to create tables we need metadata object
Base.metadata.create_all(engine)

#sample persons
person1 = "Emily"
person2 = "Elizabeth"
person3 = "Callen"

#close session 
session.close()


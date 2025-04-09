
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# Base model for SQLAlchemy
Base = declarative_base()

# Define database models - the schema is generated using these
class DataRefined(Base):
    __tablename__ = 'data'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(String, nullable=False)
    files = Column(Integer, nullable=False)
    owner = Column(String, nullable=False)

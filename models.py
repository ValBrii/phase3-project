from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Description(Base):
    __tablename__ = 'description'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Establish one-to-many relationship with Note
    notes = relationship("Note", back_populates="description")

class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    description_id = Column(Integer, ForeignKey('description.id'))

    # Relationship to Description
    description = relationship("Description", back_populates="notes")

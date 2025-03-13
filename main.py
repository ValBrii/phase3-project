from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker
import click

Base = declarative_base()

# Define the Category model
class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    # Relationship with Note
    notes = relationship("Note", back_populates="category")

# Define the Note model
class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'))

    # Relationship to Category
    category = relationship("Category", back_populates="notes")

# Database setup
engine = create_engine("sqlite:///notes.db")
SessionLocal = sessionmaker(bind=engine)

# Create the tables in the database
Base.metadata.create_all(engine)

@click.group()
def cli():
    """CLI for the Notes App"""
    pass

# Command to add a new category
@cli.command()
@click.option('--name', prompt='Category Name')
def add_category(name):
    session = SessionLocal()
    category = Category(name=name)
    session.add(category)
    session.commit()
    click.echo(f"Added category: {category.name}")
    session.close()

# Command to add a new note with a category
@cli.command()
@click.option('--title', prompt='Note Title')
@click.option('--category_id', prompt='Category ID', type=int)
def add_note(title, category):
    session = SessionLocal()
    category_obj = session.query(Category).filter(Category.id == category_id).first()

    if not category_obj:
        click.echo("Category not found. Please enter a valid category ID.")
        return

    note = Note(title=title, category=category_obj)
    session.add(note)
    session.commit()
    click.echo(f"Added note: {note.title} under category: {category_obj.name}")
    session.close()

# Command to list all notes with their categories
@cli.command()
def list_notes():
    session = SessionLocal()
    notes = session.query(Note).all()
    
    for note in notes:
        category_name = note.category.name if note.category else "Uncategorized"
        click.echo(f"ID: {note.id}, Title: {note.title}, Category: {category_name}")

    session.close()

# Command to list all categories
@cli.command()
def list_categories():
    session = SessionLocal()
    categories = session.query(Category).all()
    
    if not categories:
        click.echo("No categories found.")
    else:
        for category in categories:
            click.echo(f"ID: {category.id}, Name: {category.name}")

    session.close()

# Command to delete a note
@cli.command()
@click.option('--note-id', prompt='Note ID', type=int)
def delete_note(note_id):
    session = SessionLocal()
    note = session.query(Note).filter(Note.id == note_id).first()
    
    if note:
        session.delete(note)
        session.commit()
        click.echo(f"Deleted note with ID: {note_id}")
    else:
        click.echo("Note not found!")

    session.close()

if __name__ == '__main__':
    cli()

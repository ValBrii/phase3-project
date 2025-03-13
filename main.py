from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import click
from models import Category, Note, Base

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

# Command to add a new note with title, content, and category
@cli.command()
@click.option('--title', prompt='Note Title')
@click.option('--content', prompt='Note Content')
@click.option('--category_id', prompt='Category ID', type=int)
def add_note(title, content, category_id):
    session = SessionLocal()
    category_obj = session.query(Category).filter(Category.id == category_id).first()

    if not category_obj:
        click.echo("Category not found. Please enter a valid category ID.")
        return

    note = Note(title=title, content=content, category=category_obj)
    session.add(note)
    session.commit()
    click.echo(f"Added note: {note.title} with content: {note.content} under category: {category_obj.name}")
    session.close()

# Command to list all notes with their categories and content
@cli.command()
def list_notes():
    session = SessionLocal()
    notes = session.query(Note).all()

    for note in notes:
        category_name = note.category.name if note.category else "Uncategorized"
        click.echo(f"ID: {note.id}, Title: {note.title}, Content: {note.content}, Category: {category_name}")

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


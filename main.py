from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import click
from models import Note, Description, Base  # Import Base from your model.py

# Database setup

engine = create_engine("sqlite:///notes.db")
SessionLocal = sessionmaker(bind=engine)

# Create the tables in the database
Base.metadata.create_all(engine)  # This will create the tables in the database if they don't exist

@click.group()
def cli():
    """
    CLI for the Notes App
    """
    pass

# Command to add a new note
@cli.command()
@click.option('--title', prompt='Note Title')
@click.option('--content', prompt='Note Content')
@click.option('--description-id', prompt='Description ID', type=int)
def add_note(title, content, description_id):
    session = SessionLocal()
    description = session.query(Description).filter(Description.id == description_id).first()

    if not description:
        click.echo("Description not found. Please create one first.")
        session.close()
        return

    note = Note(title=title, content=content, description=description)
    session.add(note)
    session.commit()
    click.echo(f"Added note: {note.title}")
    session.close()

# Command to add a new description
@cli.command()
@click.option('--name', prompt='Description Name')
def add_description(name):
    session = SessionLocal()
    description = Description(name=name)
    session.add(description)
    session.commit()
    click.echo(f"Added description: {description.name}")
    session.close()

# Command to list all notes
@cli.command()
def list_notes():
    session = SessionLocal()
    notes = session.query(Note).all()
    for note in notes:
        description_name = note.description.name if note.description else "No Description"
        click.echo(f"ID: {note.id}, Title: {note.title}, Content: {note.content} | Description: {description_name}")
    session.close()

# Command to list all descriptions
@cli.command()
def list_descriptions():
    session = SessionLocal()
    descriptions = session.query(Description).all()
    for desc in descriptions:
        click.echo(f"ID: {desc.id}, Name: {desc.name}")
    session.close()

# Command to delete a note
@cli.command()
@click.option('--note-id', prompt='Note ID', type=int)
def delete_note(note_id):
    session = SessionLocal()
    note = session.query(Note).filter(Note.id == note_id).first()

    if not note:
        click.echo("Note not found.")
        session.close()
        return

    session.delete(note)
    session.commit()
    click.echo(f"Deleted note with ID: {note_id}")
    session.close()

if __name__ == '__main__':
    cli()

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Note, Description, Base

# Database setup
engine = create_engine("sqlite:///notes.db")
SessionLocal = sessionmaker(bind=engine)

# Create tables if they don't exist
Base.metadata.create_all(engine)

# Add a new note
def add_note():
    session = SessionLocal()
    description_id = 1  # You can modify this as needed
    description = session.query(Description).filter(Description.id == description_id).first()

    if not description:
        print("Description not found. Please create one first.")
        session.close()
        return

    # Create a new note
    title = "Sample Note Title"
    content = "This is the content of the sample note."

    note = Note(title=title, content=content, description=description)
    session.add(note)
    session.commit()
    print(f"Added note: {note.title}")
    session.close()

# View all existing notes
def view_notes():
    session = SessionLocal()
    notes = session.query(Note).all()
    if notes:
        for note in notes:
            description_name = note.description.name if note.description else "No Description"
            print(f"ID: {note.id}, Title: {note.title}, Content: {note.content} | Description: {description_name}")
    else:
        print("No notes found.")
    session.close()

# Delete a note
def delete_note():
    session = SessionLocal()
    note_id = 1  # Change to the ID of the note you want to delete
    note = session.query(Note).filter(Note.id == note_id).first()

    if not note:
        print(f"Note with ID {note_id} not found.")
        session.close()
        return

    session.delete(note)
    session.commit()
    print(f"Deleted note with ID: {note_id}")
    session.close()


# Main execution
if __name__ == "__main__":
    # Adding a note
    add_note()

    # Viewing all notes
    view_notes()

    # Deleting a note
    delete_note()


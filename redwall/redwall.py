from flask import (
    Flask,
    render_template,
)
import sqlite3
from typing import Optional
from uuid import uuid4

class Note:
    def __init__(self, title: str, content: str, id: Optional[str] = None):
        self.title = title
        self.content = content
        if id == None:
            self.id = uuid4().hex
        else:
            self.id = id

class Storage:
    def __init__(self):
        self.connection = sqlite3.connect('/Users/vincesiu/dev/redwall/redwall/redwall.db')

    def list_notes(self):
        raise NotImplementedError()

    def create_note(self, note: Note):
        cursor = self.connection.cursor()
        query = 'insert into notes (id, title, content) values ("{}", "{}", "{}")'.format(note.id, note.title, note.content)
        cursor.execute(query)
        self.connection.commit()

    def get_note(self, note_id: str) -> Optional[Note]:
        cursor = self.connection.cursor()
        query = 'select id, title, content from notes where id = "{}"'.format(note_id)
        cursor.execute(query)
        results = cursor.fetchone()
        if results == None:
           return None
        note = Note(
            title=results[1],
            content=results[2],
            id=results[0],
        )
        return note
       
    def update_note(self, note: Note) -> None:
        cursor = self.connection.cursor()
        query = 'update notes set title = "{}", content = "{}" where id = "{}"'.format(note.title, note.content, note.id)
        cursor.execute(query)
        self.connection.commit()

    def delete_note(self):
        raise NotImplementedError()


app = Flask(__name__)
storage = Storage()

@app.route('/')
def list_notes():
    return 'Hello, World!'

@app.route('/<post_id>')
def edit_note(post_id):
    import uuid
    id = UUID('840bb90445e3499a91815e11a27ea1c6')
    note = storage.get_note(id)
    assert note is not None

    return render_template("edit_note.html", title=note.title, content=note.content)

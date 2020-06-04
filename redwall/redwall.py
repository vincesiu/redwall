from flask import (
    Flask,
    render_template,
    request,
    send_file,
)
import json
import pypandoc
import sqlite3
from typing import List, Optional
from uuid import (
   uuid4,
   UUID,
)

class Note:
    def __init__(self, title: str, content: str, id: Optional[str] = None):
        self.title = title
        self.content = content
        if id == None:
            self.id = uuid4().hex
        else:
            self.id = id

    @classmethod
    def format_id_for_url(cls, url_id: str) -> str:
       return UUID(id).hex

    @classmethod
    def parse_id_from_url(cls, id: str) -> str:
        return str(UUID(id))

class Storage:
    def __init__(self):
        self.connection = sqlite3.connect('/Users/vincesiu/dev/redwall/redwall/redwall.db')

    def list_notes(self) -> List[Note]:
        cursor = self.connection.cursor()
        query = 'select id, title, content from notes'
        cursor.execute(query)
        results = cursor.fetchall()
        if results == None:
           return None
        notes = []
        for result in results:
            notes.append(Note(
                title=result[1],
                content=result[2],
                id=result[0],
            ))
        return notes

    def create_note(self, note: Note):
        cursor = self.connection.cursor()
        query = 'insert into notes (id, title, content) values (:id, :title, :content)'
        cursor.execute(query, {"id": note.id, "title": note.title, "content": note.content})
        self.connection.commit()

    def get_note(self, note_id: str) -> Optional[Note]:
        cursor = self.connection.cursor()
        query = 'select id, title, content from notes where id = :id'
        cursor.execute(query, {"id": note_id})
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
        query = 'update notes set title = :title, content = :content where id = :id'
        cursor.execute(query, {"title": note.title, "content": note.content, "id": note.id})
        self.connection.commit()

    def delete_note(self, note: Note) -> None:
        cursor = self.connection.cursor()
        query = 'delete from notes where id = :id'
        cursor.execute(query, {"id": note.id})
        self.connection.commit()

class RenderEngine:
    def __init__(self):
        pass

    def render_md_to_html(self, input_markdown: str) -> str:
        return pypandoc.convert_text(input_markdown, 'html', format='md')

app = Flask(__name__)
storage = Storage()
render_engine = RenderEngine()

from collections import namedtuple
FormattedNote = namedtuple('FormattedNote', ['href', 'caption'])


@app.route('/')
def list_notes():
    notes = storage.list_notes()
    formatted_notes = []
    for note in notes:
        formatted_notes.append(FormattedNote(
            href="./{}".format(note.id),
            caption=note.title,
        ))

    return render_template(
        "list_notes.html",
        notes=formatted_notes
        )

@app.route('/render_markdown', methods=['POST'])
def render_markdown():
    """
    will throw if "content" key is not supplied. example response

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
    <title>400 Bad Request</title>
    <h1>Bad Request</h1>
    <p>The browser (or proxy) sent a request that this server could not understand.</p>
    """
    print("render markdown called with the arguments {}".format(request.json))
    unrendered = request.json["content"]
    return json.dumps(render_engine.render_md_to_html(unrendered))

@app.route('/update_note', methods=['POST'])
def update_note():
    print("Update note called with {}".format(request.json))
    note = Note(
        title = request.json['title'],
        content = request.json['content'],
        id = request.json['note_id'],
    )
    storage.update_note(note)
    return "success"

@app.route('/create_note', methods=['GET', 'POST'])
def create_note():
    if request.method == 'GET':
        print("Create note called")
        return render_template("create_note.html")

    if request.method == 'POST':
        print("Create note called with {}".format(request.json))
        note = Note(
            title = request.json['title'],
            content = request.json['content'],
        )
        storage.create_note(note)
        return json.dumps(note.id)

@app.route('/favicon.ico')
def favicon():
    return send_file("./static/favicon.ico", as_attachment=True)

@app.route('/<post_id>')
def edit_note(post_id):
    note = storage.get_note(post_id)
    if note is None:
        raise KeyError(post_id)

    return render_template(
        "edit_note.html",
        title=note.title,
        note_id=post_id,
        unrendered_content=note.content,
        rendered_content=render_engine.render_md_to_html(note.content),
    )


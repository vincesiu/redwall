from flask import (
    Flask,
    render_template,
    request,
)
import json
import pypandoc
import sqlite3
from typing import Optional
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

class RenderEngine:
    def __init__(self):
        pass

    def render_md_to_html(self, input_markdown: str) -> str:
        return pypandoc.convert_text(input_markdown, 'html', format='md')

app = Flask(__name__)
storage = Storage()
render_engine = RenderEngine()

@app.route('/')
def list_notes():
    return 'Hello, World!'

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

@app.route('/<post_id>')
def edit_note(post_id):
    note = storage.get_note(post_id)
    assert note is not None

    return render_template(
        "edit_note.html",
        title=note.title,
        note_id=post_id,
        unrendered_content=note.content,
        rendered_content=render_engine.render_md_to_html(note.content),
    )

@app.route('/save_note', methods=['POST'])
def save_note():
    print("save note called with {}".format(request.json))
    note = Note(
        title = request.json['title'],
        content = request.json['content'],
        id = request.json['note_id'],
    )
    storage.update_note(note)
    return "success"

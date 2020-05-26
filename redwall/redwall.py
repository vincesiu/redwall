from flask import (
    Flask,
    render_template,
)

app = Flask(__name__)

@app.route('/')
def list_notes():
    return 'Hello, World!'

@app.route('/<post_id>')
def edit_note(post_id):
    return render_template("edit_note.html", post_id=post_id)

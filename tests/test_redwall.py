import sys
sys.path.insert(0, '../') # Required for Redwall import

from redwall import __version__
from redwall.redwall import Note, RenderEngine, Storage


def test_version():
    assert __version__ == '0.1.0'

def test_note_creation():
    title = "fake_testing_title"
    content = "fake_testing_content"
    note = Note(
            title = title,
            content = content,
    )
    assert note.id is not None
    assert note.title == title
    assert note.content == content

def test_db_create_and_get():
    s = Storage()
    title = "fake_testing_title"
    content = "fake_testing_content"
    note1 = Note(
            title = title,
            content = content,
    )
    s.create_note(note1)
    note2 = s.get_note(note1.id)
    assert note1.title == note2.title
    assert note1.content == note2.content
    assert note1.id == note2.id

def test_db_create_and_get_and_update():
    s = Storage()
    title = "fake_testing_title"
    content = "fake_testing_content"
    note1 = Note(
            title = title,
            content = content,
    )
    s.create_note(note1)

    new_title =  "new_fake_testing_title"
    new_content = "new_fake_testing_content"
    note1.title = new_title
    note1.content = new_content
    s.update_note(note1)
    note2 = s.get_note(note1.id)
    assert note2.title == new_title
    assert note2.content == new_content

def test_db_create_and_delete():
    s = Storage()
    note1 = Note(
        title = "fake_testing_title",
        content ="fake_testing_content",
    )
    s.create_note(note1)
    note2 = s.get_note(note1.id)
    s.delete_note(note1)
    note3 = s.get_note(note1.id)
    assert note3 is None

def test_render_engine():
    r = RenderEngine()
    markdown = "hello world"
    html = r.render_md_to_html(markdown)
    assert html == "<p>hello world</p>\n"

if __name__ == '__main__':
    run_all_tests()

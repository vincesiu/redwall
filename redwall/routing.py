from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    # query sqlite3 for list of all post_ids, title, ctime, mtime, atime
    return 'Hello, World!'

@app.route('/<post_id>')
def generate_post(post_id):
    # given post_id, get the title, ctime, mtime, atime
    # update atime
    html = """\
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>Redwall</title>
</head>

<body>
Hello world
post id: {post_id}

<div id="input">
   <form style="width:auto;"action="/meow" id="usrform">
  Name: <input type="text" name="usrname">
  <input type="submit">
</form>  
</div>
<div id="output">
</div>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<script>
    document.getElementById('output').innerHTML =
      marked('# Marked in the browser\\n\\nRendered by **marked**.');
</script>
</body>
</html>
""".format(post_id=post_id)
    return html
#    "document.getElementById('output').innerHTML = marked(document.getElementById('input2').value)"


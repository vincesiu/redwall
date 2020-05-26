[x] initialize git repo frontend setup 
[x] [front] create jinja templating + send the template in the edit endpoint
  - tested by seeing that I can edit the Jinja template in the frontend

## CRUD and persisting files
[x] [server] create db struct and define interface to backend, hooking this up to the edit flow
  - list_notes, get_note, update_note, create_note, search_notes, delete_note
  - tested by putting static requests in the backend and returning those
  - title, content
[x] [server] add sqlite3 database with table of markdown files
  - create db, add to gitignore
  - adding a initialize.db script
[x] [server][edit] implement reads from the sqlite3 database
  - statically create some files in the sqlite3 database
  - implement get_note
[ ] [frontend][edit] implement reads
  - populate the html file textarea with the right thing in Jinja
[ ] [server] on initial read, implement function to send markdwon to html in pandoc
  - function that receives markdown string and renders to html
[ ] [frontend][edit] on load of a note, render the markdown server side
  - populate the html file textarea with the right thing in Jinja
[x] [server][edit] implement updates to the sqlite3 database
  - implement that dank write endpoint, update_note
  - add post endpoint
  - be able to edit the title or the content
[ ] [frontend][edit] impleemnt updates
  - add fetch usage in the frontend
  - update the title or the content
  - onchange, send the contents of that textarea to the backend
[ ] [server] implement main page to query list of all the current notes, hyperlinked
  - need to implement db class
  - add new sqlite3 query
[ ] [front] implement main page to display list of all current notes
  - create new jinja template
[x] [server][edit] implement creates to the sqlite3 database]
  - implement that dank write endpoint, create_note
  - add post endpoint
[ ] [frontend][edit] impleemnt creates
  - make this a separate html page
  - add new button in the main page to create
  - auto-redirect to the edit page
  - add fetch usage in the frontend
  - onchange, send the contents of that textarea to the backend

## change the html parser
[ ] [server] add new post endpoint to receive + send back markdown parsed as html
  - be able to send markdown, return html
[ ] [front] post query to markdown -> other parser
  - change the frontend parser from the markdown js library to this
[ ] [front] implement debouncing
  - trailing edge probably

## wishlist
[ ] [server] autosave
[ ] [server][edit] change the post_id from route to the get parameter
[ ] [front] markdown css
[ ] [front] overall page css
[ ] [server] add extra fields 
  - atime, ctime, mtime, tags
[ ] [frontend] display extra fields
  - ctime
  - mtime
[ ] [frontend] add tags
[ ] [frontend] add searching by tags and by title
[ ] [server] 404 or some other error handling if the post_id does not exist
[ ] [frontend] 404 error page if the post_id does not exist
[ ] [server] see what happens if an exception is thrown - 504 or something?


[ ] [server] delete note
  - implement db endpoint to delete note
[ ] [frontend] delete note
  - button to send request + confirmation to delete note
  - send request to backend
  - redirect page back to main

## goals
[ ] see all existing notes sorted in chronological order, in order of creation
  - sort by differen parameters (ctime atime mtime)
  - search by title/tag/content
[ ] create new notes
[ ] read / update existing notes
[ ] google keep but controlled by me
[ ] used for TIL, quick archiving of things I have learned
[ ] start server, and then be able to update / save 
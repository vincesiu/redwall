function createNoteWrapper(event) {
    event.preventDefault();
    var title = document.getElementById('input_title').value;
    var content = document.getElementById('input_content').value;
    var promise = createNote(title, content);
    promise.then(function(response) {
        return response.json();
    }).then(function(data) {
        window.location.href = `./${data}`;
    });

}

function createNote(title, content)  {
    return fetch('./create_note', {
        method:'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'title': title,
            'content': content,
        })
    });
};

function updateNoteWrapper(event) {
    var title = document.getElementById('input_title').value;
    var content = document.getElementById('input_content').value;
    var note_id = document.getElementById('input_note_id').innerHTML;
    var promise = updateNote(note_id, title, content);
    promise.then(function(response) {
      console.log('Successfully updated note id:', document.getElementById('input_note_id').innerHTML);
    });
    
}

function updateNote(event)  {
    return fetch('./update_note', {
        method:'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'title': document.getElementById('input_title').value,
            'content': document.getElementById('input_content').value,
            'note_id': document.getElementById('input_note_id').innerHTML
        })
    });
};

function deleteNoteWrapper(event) {
    var c = confirm("Are you sure you want to delete this note?");
    console.log(c);
    if (c === true) {
        var promise = deleteNote(event.target.id);
        promise.then(function(response) {
            window.location.href = './';
        });
    }
}

function deleteNote(note_id) {
    return fetch('./delete_note', {
        method:'post',
        headers: {
        'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'note_id': note_id
        })
    });
}


function updateNoteTitle(event) {
    document.getElementById('output_title').innerHTML = document.getElementById('input_title').value;
}

function renderMarkdown(event) {
    fetch('./render_markdown', {
    method: 'post',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({content: event.target.value})
  }).then(function(response) {
      console.log('Markdown rendered to html: ', response);
    return response.json();
  }).then(function(data) {
      document.getElementById('output_content').innerHTML = data;
  });
};

function debounce(fn, interval) {
    var timeoutId = undefined;
    return function (event) {
        if (timeoutId !== undefined) {
            clearTimeout(timeoutId); 
        }

        timeoutId = setTimeout(() => {
            fn(event); 
            timeoutId = undefined;
        }, interval);
   }
}

function throttle(fn, interval) {
    // action is executed on trailing edge
    var timeoutId = undefined;
    return function (event) {
        if (timeoutId !== undefined) {
            return;
        }

        timeoutId = setTimeout(() => {
            fn(event); 
            timeoutId = undefined;
        }, interval);
   }
}

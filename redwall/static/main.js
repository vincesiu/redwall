function createNote(event)  {
    event.preventDefault();
    fetch('./create_note', {
        method:'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'title': document.getElementById('input_title').value,
            'content': document.getElementById('input_content').value,
        })
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        window.location.href = `./${data}`;
    });
};

function updateNote(event)  {
    fetch('./update_note', {
        method:'post',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'title': document.getElementById('input_title').value,
            'content': document.getElementById('input_content').value,
            'note_id': document.getElementById('input_note_id').innerHTML
        })
    }).then(function(response) {
      console.log('Successfully updated note id:', document.getElementById('input_note_id').innerHTML);
    })
};

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

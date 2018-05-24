## Goal of this lesson

* Introduction to HTML `<form/>`
* Add support to the web app to accept `POST`
* Get data from the `POST` and insert new data into the database

## Introduction to HTML `<form/>`

open up `kittens.html`, add the following right under the first `<div>`
```
  <form method="post">
    <input type="text" name="name"/>
    <input type="text" name="url"/>
    <input type="submit" name="new_url" class="btn btn-primary"/>
  </form>
```

Refresh your page and you should see a button.  Click on it and see what happens

### What does this mean?

The HTML `<form>` element is one of the most common way for browser to send data to the server.
Each `<input>` is a distinct data element that will be send to the server.
In our example, we want to send 2 things: a `name` and a `url` for your new image
The `type` attribute inside the `<input>` element denotes the type of the data.  There are a few accepted types but don't worry about it for now.
A `type="submit"` is the button.  When clicked, the data inside `<input type="text" name="name"/>` and `<input type="text" name="url"/>` will be sent (`POST`ed) to the server


## Add support to the web app to accept `POST`

open up `routes.py`:

Replace this:
```
@app.route('/kittens')
```
with this:
```
@app.route('/kittens', methods=['GET', 'POST'])
```

### What does this mean?

By default, your endpoint only accepts `GET`.  If you `POST` to this endpoint, you will get a `405 Method Not Allowed` error.

Adding `methods=['GET', 'POST']` to the route allows this endpoint to accept both `GET` and `POST`

Refresh your page and you should see a button.  Click on it and see what happens

## handling the `POST`

First add some new `import` at the top of `routes.py`:
```
from app import app
from app import db
from app.models.kitten import Kitten
from flask import render_template
from flask import request
from flask import redirect, url_for
```

Then in your `def kittens()`, add code to support the `POST`:
```
@app.route('/kittens', methods=['GET', 'POST'])
def kittens():
  if request.method == 'POST':
    new_kitten = Kitten(name=request.form['name'], url=request.form['url'])
    db.session.add(new_kitten)
    db.session.commit()
    return redirect(url_for('kittens'))
  else:        
    return render_template('kittens.html', kittens=Kitten.query.all())
```



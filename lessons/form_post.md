## Goal of this lesson

* Introduction to HTML `<form/>`
* Add support to the web app to accept `POST`
* Get data from the `POST` and insert new data into the database
* Bonus - style the page

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

Refresh your page and click on the button and see what happens

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

Then inside your `def kittens()` method, add logic to support the `POST`:
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

### What does this mean?

Now that the endpoint can accept both `GET` and `POST`, we need different logic to handle each method.

This is a standard `if ... else ...`.  The `else` case just runs our existing logic that returns an HTML.

The `if request.method == 'POST':` case handles the `POST` data coming from the browser.  Without going into syntax detail, the code is basically doing the following:

* Get the 2 distinct data element from the `POST` - `request.form['name']` and `request.form['url']`
* Create a new `Kitten` object and set the `name` and `url` attribute using the data from the `POST`
* Persist (insert) the new `Kitten` object into the database
* returns a `redirect` to the browser to reload the page

Refresh your page, enter some data in the first text box, enter a valid url in the second box, then click the button.

## Bonus - style the page

open up `kittens.html`, add the following inside the `<head>` element:

```
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
```

Refresh your page, you should see some slight different in the default fonts.

More to come!

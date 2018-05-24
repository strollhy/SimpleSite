## Goal of this lesson

* Introduction to HTML `<form/>`
* Add support to the web app to accept `POST`
* Get data from the `POST` and insert new data into the database

## Introduction to HTML `<form/>`

open up kittens.html, add the following right under the first `<div>`
```
  <form method="post">
    <input type="text" name="name"/>
    <input type="text" name="url"/>
    <input type="submit" name="new_url" class="btn btn-primary"/>
  </form>
```

### What does this mean?

The HTML `<form>` element is one of the most common way for browser to send data to the server.
Each `<input>` is a distinct data element that will be send to the server.
In our example, we want to send 2 things: a `name` and a `url` for your new image
The `type` attribute inside the `<input>` element denotes the type of the data.  There are a few accepted types but don't worry about it for now.
A `type="submit"` is the button.  When clicked, the data inside `<input type="text" name="name"/>` and `<input type="text" name="url"/>` will be sent (`POST`ed) to the server


routes.py

```
@app.route('/kittens')
```
add support for POST
```
@app.route('/kittens', methods=['GET', 'POST'])
```

handle the POST
```
    if request.method == 'POST':
        return render_template('kittens.html', kittens=Kitten.query.all())
	return redirect(url_for('kittens'))
    else:        
        return render_template('kittens.html', kittens=Kitten.query.all())
```



# Add a form

kittens.html
```
    <form method="post">
        <input type="text" name="name"/>
	<input type="text" name="url"/>
	<input type="submit" name="new_url" class="btn btn-primary"/>
    </form>
```

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



# SimpleSite
A simple site built with Flask.  
Make sure you run the app under virtual env: `source venv/bin/activate`

# To setup the database
1. ```brew install mysql```

2. ```brew services start mysql```

3. ```./setup_db.sh```

4. Update permission in case you can't run `setup_db.sh`:  
```chmod +x setup_db.sh```

# To run the app
1. Start the app:  
```./start_app.sh```

1. Update permission in case you can't run `start_app.sh`:  
```chmod +x start_app.sh```

1. ```open http://localhost:5000/```

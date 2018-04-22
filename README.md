# SimpleSite
A simple site built with Flask.  

# Setup environment
```
sudo easy_install pip
sudo pip install virtualenv

virtualenv venv
source venv/bin/activate

pip install Flask
pip install flask-sqlalchemy
pip install mysql-python
```

# Setup database
```
brew install mysql
brew services start mysql
./setup_db.sh
```

Update permission in case you can't run `setup_db.sh`:  ```chmod +x setup_db.sh```

# Run the app
```./start_app.sh```

Update permission in case you can't run `start_app.sh`:  ```chmod +x start_app.sh```

```open http://localhost:5000/```

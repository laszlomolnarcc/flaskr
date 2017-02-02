# Flaskr with peewee example

This is the same flaskr what can be found here

[http://flask.pocoo.org/docs/0.12/tutorial/](http://flask.pocoo.org/docs/0.12/tutorial/)

but made with peewee as ORM. You are welcome. :)

# How it works?

1. clone this git repository (obviously)
2. go to the directory where this README.md is located what you are reading now
3. run this command:

`sudo pip3 install --editable .`

4. If it runs without error (means: no red text), run these:

`export FLASK_APP=flaskr`

`export FLASK_DEBUG=true`

5. create the database with this command:

`flask initdb`

6. finally, start the application:

`flask run`

Ideally this should start the server, and now you can reach it from your browser on this address:

[http://127.0.0.1:5000/](http://127.0.0.1:5000/)


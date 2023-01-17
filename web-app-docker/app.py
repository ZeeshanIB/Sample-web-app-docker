import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@host:port/dbname'
db = SQLAlchemy(app)

class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip_address = db.Column(db.String(255))

@app.route('/')
def index():
    ip = request.remote_addr
    connection = Connection(ip_address=ip)
    db.session.add(connection)
    db.session.commit()
    return 'IP address saved: {}'.format(ip)

if _name_ == '_main_':
    app.run(host="0.0.0.0", port=8080)







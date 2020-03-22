import psycopg2
from flask import Flask, request, url_for, redirect
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy #por algun otibo no reconose el proseso create_engine

DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user="postgres",pw="Perros2012",url="animalicis.crl39vc3ngno.us-east-2.rds.amazonaws.com",db="animalicis")

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User_(db.Model):
    name= db.Column(db.String(80), nullable=False)
    lastname= db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    pw_hash= db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.name


class Refuge_(db.Model):
    name= db.Column(db.String(80), nullable=False)
    email= db.Column(db.String(120), unique=True, nullable=False, primary_key=True)
    pw_hash= db.Column(db.String(80), nullable=False)
    department= db.Column(db.String(80), nullable=False)
    city= db.Column(db.String(80), nullable=False)
    neighborhood= db.Column(db.String(80), nullable=False)
    Googlemaps= db.Column(db.String(80), nullable=False)
    description= db.Column(db.String(140))
    rep= db.Column(db.String(80), nullable=False)
    phone= db.Column(db.Integer)
    celphone= db.Column(db.Integer, nullable=False)
    website= db.Column(db.String(80))
    animal= db.Column(db.String(80), nullable=False)
    time_o= db.Column(db.String(5), nullable=False)
    time_c= db.Column(db.String(5), nullable=False)
    photo= db.Column(db.String(140))

    def __repr__(self):
        return '<User %r>' % self.name

class Animals_(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(120), nullable=False)
    name= db.Column(db.String(80), nullable=False)
    age= db.Column(db.String(80), nullable=False)
    breed= db.Column(db.String(80), nullable=False)
    gender= db.Column(db.String(80), nullable=False)
    health= db.Column(db.String(80), nullable=False)
    coments= db.Column(db.String(80), nullable=False)
    type= db.Column(db.String(80), nullable=False)
    photo= db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return '<Animals %r>' % self.breed

if __name__ == '__main__':
    app.run(debug=True)

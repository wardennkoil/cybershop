from sqlalchemy.dialects.postgresql import ARRAY
from config import db
import os
import json


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(30))
    name = db.Column(db.String(150), nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    platform = db.Column(db.String(30), nullable=False)
    developers = db.Column(db.String(30))
    genre = db.Column(db.String(40), nullable=False)
    game_description = db.Column(db.Text, nullable=False)
    min_requirements = db.Column(db.Text, nullable=False)
    sug_requirements = db.Column(db.Text, nullable=False)


    def __repr__(self):
        return '<Game %r>' % self.id

db.create_all()
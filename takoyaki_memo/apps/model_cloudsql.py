# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

builtin_list = list

db = SQLAlchemy()

def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)

def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data

class TakoyakiMemo(db.Model):
    __tablename__ = 'memo'

    id = db.Column(db.String, primary_key=True)
    text = db.Column(db.Text)
    created_at = db.Column(db.Integer)

    def __repr__(self):
        return "<Memo(id=%s, text=%s)" % (self.id, self.text)

def read(id):
    result = TakoyakiMemo.query.get(id)
    if not result:
        return None
    return from_sql(result)

def create(data):
    t_memo = TakoyakiMemo(**data)
    db.session.add(t_memo)
    db.session.commit()
    return from_sql(t_memo)

def delete(id):
    TakoyakiMemo.query.filter_by(id=id).delete()
    db.session.commit()

def _create_database():
    """
    If this script is run directly, create all the tables necessary to run the
    application.
    """
    app = Flask(__name__)
    app.config.from_pyfile('./config.py')
    init_app(app)
    with app.app_context():
        db.create_all()
    print("All tables created")


if __name__ == '__main__':
    _create_database()

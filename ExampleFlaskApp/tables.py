from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Libros(db.Model):
    __tablename__ = "libros"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String, nullable=False, unique=True)
    titulo = db.Column(db.String, nullable=False)
    autor = db.Column(db.String, nullable=False)
    año = db.Column(db.String, nullable=False)
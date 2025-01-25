# import sqlite3
# 
# db = sqlite3.connect("books-collection.db")
# 
# cursor = db.cursor()
# 
# #cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# 
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# 
# db.commit()

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

# Create Database
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"

# Create extension
db = SQLAlchemy(model_class=Base)

# Initialise app with extension
db.init_app(app)


# Create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key = True)
    title: Mapped[str] = mapped_column(String(250),unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250),nullable=False)
    rating: Mapped[int] = mapped_column(Float,nullable=False)

# Create table schema in database. Requires application context.
with app.app_context():
    db.create_all()

# Create record
with app.app_context():
    new_book = Book(id=1, title = "Harry Potter", author = "J. K. Rowling", rating = 9.3)
    db.session.add(new_book)
    db.session.commit()
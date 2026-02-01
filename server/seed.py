#!/usr/bin/env python3

from faker import Faker
import os
from config import create_app, db
from models import Book

fake = Faker()

env = os.getenv("FLASK_ENV", "dev")
app = create_app(env)

with app.app_context():
    print("Deleting all books...")
    Book.query.delete()

    print("Creating books...")
    books = []

    for _ in range(500):
        book = Book(
            title=fake.sentence(nb_words=4),
            author=fake.name(),
            description=fake.paragraph(nb_sentences=5)
        )
        books.append(book)

    db.session.add_all(books)
    db.session.commit()
    print("Complete.")

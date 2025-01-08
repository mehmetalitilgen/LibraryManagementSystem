
from services.book_service.models.book_model import Book
from services.common.config import db

def get_book(book_id):
    book = Book.query.get(book_id)
    if book:
        return {"id":book.id,"title":book.title,"author":book.author}
    return None

def create_book(data):
    print("deneme123")
    book = Book(title=data["title"],author=data["author"])
    db.session.add(book)
    db.session.commit()
    return {"id":book.id,"title":book.title,"author":book.author}

def update_book(book_id,data):
    book = Book.query.get(book_id)
    if not book:
        return None
    book.title = data.get("title",book.title)
    book.author = data.get("author",book.author)
    db.session.commit()
    return {"id":book.id,"title":book.title,"author":book.author}

def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return None
    db.session.delete(book)
    db.session.commit()
    return {"id":book.id,"title":book.title,"author":book.author}

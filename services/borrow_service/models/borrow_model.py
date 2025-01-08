from services.common.config import db
from datetime import date

class BorrowRecord(db.Model):
    __tablename__ = "borrow_records"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    book_id = db.Column(db.Integer, nullable=False)
    borrow_date = db.Column(db.Date, default=date.today, nullable=False)
    return_date = db.Column(db.Date, nullable=True)

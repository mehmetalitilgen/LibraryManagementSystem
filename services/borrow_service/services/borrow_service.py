from services.borrow_service.models.borrow_model import BorrowRecord
from services.common.config import db


def get_borrow_record(borrow_id):
    borrow_record = BorrowRecord.query.get(borrow_id)
    if borrow_record:
        return {"id": borrow_record.id, "user_id": borrow_record.user_id, "book_id": borrow_record.book_id,
                "borrow_date": borrow_record.borrow_date, "return_date": borrow_record.return_date}
    return None


def create_borrow_record(data):
    borrow_record = BorrowRecord(
        user_id=data["user_id"],
        book_id=data["book_id"],
        borrow_date=data["borrow_date"],
        return_date=data["return_date"],
    )
    db.session.add(borrow_record)
    db.session.commit()
    return {"id": borrow_record.id, "user_id": borrow_record.user_id, "book_id": borrow_record.book_id,
            "borrow_date": borrow_record.borrow_date, "return_date": borrow_record.return_date}


def update_borrow_record(borrow_id, data):
    borrow_record = BorrowRecord.query.get(borrow_id)
    if not borrow_record:
        return None

    borrow_record.user_id = data.get("user_id", borrow_record.user_id)
    borrow_record.book_id = data.get("book_id", borrow_record.book_id)
    borrow_record.borrow_date = data.get("borrow_date", borrow_record.borrow_date)
    borrow_record.return_date = data.get("return_date", borrow_record.return_date)
    db.session.commit()
    return {"id": borrow_record.id, "user_id": borrow_record.user_id, "book_id": borrow_record.book_id, "borrow_date": borrow_record.borrow_date, "return_date": borrow_record.return_date}

def delete_borrow_record(borrow_id):
    borrow_record = BorrowRecord.query.get(borrow_id)
    if not borrow_record:
        return False
    db.session.delete(borrow_record)
    db.session.commit()
    return True
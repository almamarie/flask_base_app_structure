from sqlalchemy.orm import Session


def create_item(session: Session, item):
    session.add(item)
    session.commit()
    return item


def get_all_items(session: Session, model):
    return session.query(model).all()


def get_item_by_id(session: Session, model, item_id):
    return session.query(model).filter_by(id=item_id).first()


def update_item(session: Session, item, new_data):
    for key, value in new_data.items():
        setattr(item, key, value)
    session.commit()


def delete_item(session: Session, item):
    session.delete(item)
    session.commit()

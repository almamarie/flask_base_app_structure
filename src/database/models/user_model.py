from sqlalchemy import Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from ...utils.crud import create_item, get_all_items, get_item_by_id, update_item, delete_item
from ..database import db

# Base = declarative_base()


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(50))

    @classmethod
    def create_user(cls, session, username, email):
        new_user = cls(username=username, email=email)
        return create_item(session, new_user)

    @classmethod
    def get_all_users(cls, session):
        return get_all_items(session, cls)

    @classmethod
    def get_user_by_id(cls, session, user_id):
        return get_item_by_id(session, cls, user_id)

    def update_user(self, session, new_data):
        update_item(session, self, new_data)

    def delete_user(self, session):
        delete_item(session, self)

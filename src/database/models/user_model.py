from sqlalchemy import Column, String, UUID, Date
import hashlib
import secrets
from datetime import datetime
from ...utils.crud import create_item, get_all_items, get_item_by_id, update_item, delete_item
from ...utils.generate_id import generate_id
from ..database import db


class User(db.Model):
    __tablename__ = 'users'

    userId = Column(UUID, primary_key=True, default=generate_id())
    firstName = Column(String(50))
    lastName = Column(String(50))
    otherNames = Column(
        String(50),
        nullable=True)

    birthdate: Column(Date, nullable=False)

    # TODO - Check on how to validate a column
    gender: Column(String, nullable=False, unique=True
                   # validate: {
                   #   isIn: {
                   #     args: [['M', 'F']],
                   #     msg: 'Gender must be M or F',
                   #   },
                   # },
                   )

    country: Column(String, nullable=False, unique=False)

    email: Column(String, nullable=False, unique=True)

    address: Column(String, nullable=False)

    profilePicture: Column(String, nullable=False)

    passwordHash: Column(String, nullable=False)

    passwordResetToken: Column(String, nullable=True)

    passwordResetExpires: Column(Date, nullable=False)

    passwordChangedAt: Column(Date, nullable=False, default=datetime.now())

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

    def format(self):
        return {
            "userId": self.userId,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "otherNames": self.otherNames,
            "birthdate": self.birthdate,
            "gender": self.gender,
            "country": self.country,
            "email": self.email,
            "address": self.address,
            "profilePicture": self.profilePicture
        }

    def createPasswordResetToken(self):
        reset_token = secrets.token_hex(32)

        reset_token = hashlib.sha256(reset_token.encode()).hexdigest()

        self.passwordResetToken = reset_token

        print({reset_token}, self.passwordResetToken)

        self.passwordResetExpires = Date.now() + 10 * 60 * 1000

        return reset_token

    # TODO -  check on how to parse an int in python an use to update the below
    # def changedPasswordAfter (self, JWTTimestamp):
    #     if self.updatedAt and self.passwordChangedAt:
    #         changedTimestamp = parseInt( self.passwordChangedAt.getTime() / 1000, 10)
    #         return JWTTimestamp < changedTimestamp

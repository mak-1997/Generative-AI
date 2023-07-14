# from application import db
from mongoengine import (
    Document,
    StringField,
    IntField,
    BooleanField,
    ReferenceField,
    ListField,
)


class Dish(Document):
    dish_name = StringField(required=True)
    dish_price = IntField(required=True)
    dish_availability = BooleanField(default=True)


class User(Document):
    user_name = StringField(required=True)
    user_email = StringField(required=True)
    user_password = StringField(required=True)


class Admin(Document):
    admin_name = StringField(required=True)
    admin_email = StringField(required=True)
    admin_password = StringField(required=True)
    is_admin = BooleanField(default=True)


class Order(Document):
    user_id = ReferenceField(User)
    dish_ids = ListField(ReferenceField(Dish))
    status = StringField(default="Order Received")

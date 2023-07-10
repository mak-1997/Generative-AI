from app import db

class Dish(db.Document) :
    dish_id = db.StringField(required = True)
    dish_name = db.StringField(req)
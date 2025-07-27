from mongoengine import Document,StringField

class user(Document):
    full_name = StringField(required = True)
    email = StringField(required = True)
    password = StringField(required = True)
    
from mongoengine import Document,StringField

class Role(Document):
    name = StringField(min_length=3, max_length=50, required=True)
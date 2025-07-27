from mongoengine import Document,StringField,IntField,FloatField

class clothe(Document):
    Size = StringField(required = True)
    Color = StringField(required = True)
    Price = IntField(required = True)
    Height = FloatField(required = False)
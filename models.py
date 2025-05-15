from mongoengine import Document, StringField, EmailField, ReferenceField, ListField, connect, ObjectIdField
import datetime

class User(Document):
    user_id = ObjectIdField(primary_key=True, default=ObjectId)
    username = StringField(required=True, unique=True, max_length=50)
    password = StringField(required=True)
    email = EmailField(required=True, unique=True)
    role = StringField(required=True, choices=('user', 'admin'), default='user')
    created_at = StringField(default=lambda: datetime.datetime.utcnow().isoformat())
    updated_at = StringField(default=lambda: datetime.datetime.utcnow().isoformat())

    meta = {
        'collection': 'users',
        'indexes': [
            'username',
            'email',
            'user_id'
        ]
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow().isoformat()
        return super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.username

class Process(Document):
    process_id = ObjectIdField(primary_key=True, default=ObjectId)
    user_id = ReferenceField(User, required=True)
    image = StringField(required=True)
    model = StringField(required=True)
    classify = StringField(required=True)
    oiliness = StringField()
    acne_level = StringField()
    created_at = StringField(default=lambda: datetime.datetime.utcnow().isoformat())
    updated_at = StringField(default=lambda: datetime.datetime.utcnow().isoformat())

    meta = {
        'collection': 'processes',
        'indexes': [
            'user_id'
        ]
    }

    def save(self, *args, **kwargs):
        self.updated_at = datetime.datetime.utcnow().isoformat()
        return super(Process, self).save(*args, **kwargs)

    def __str__(self):
        return f"Process for user {self.user_id} - Image: {self.image[:30]}"

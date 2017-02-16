from app import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    signature = db.Column(db.String(255))
    body = db.Column(db.Text)
    slug = db.Column(db.String(255), unique=True)
    owner_id = db.Column(db.String(255))

    def __str__(self):
        return self.slug

    def __init__(self, title, signature, body, slug, owner_id):
        self.title = title
        self.signature = signature
        self.body = body
        self.slug = slug
        self.owner_id = owner_id

    def is_owner(self, user_id=None):
        return self.owner_id == user_id

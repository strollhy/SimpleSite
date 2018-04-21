from app import db

class Kitten(db.Model):
    __tablename__ = 'kittens'

    # columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    url = db.Column(db.String(256))

    # serializer
    def __repr__(self):
        return "%d, %s, %s" % (self.id, self.name, self.url)

from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    # create to_dict

    def to_dict(self):
        return dict(id = self.id,
        title = self.title,
        description = self.description)

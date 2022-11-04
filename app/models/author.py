from app import db

# An author should have the following attributes with the specified types:

#     id, integer, primary key
#     name, string.



class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    # One to many relationship
    books = db.relationship("Book", back_populates="author")

    def to_dict(self):
        return dict(id = self.id,
        title = self.name)


# create_db.py


from app import db

# from models import Post
class models:
    class Post(db.Model):
        __table_args__ = {"extend_existing": True}
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        text = db.Column(db.String, nullable=False)

        def __init__(self, title, text):
            self.title = title
            self.text = text

        def __repr__(self):
            return f"<title {self.title}>"


# create the database and the db table
db.create_all()

# commit the changes
db.session.commit()

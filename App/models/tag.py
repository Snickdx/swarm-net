from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# init db
db = SQLAlchemy()


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(300), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
        

    def __repr__(self):
        return f"{self.text}"


    def toDict(self):
        return {
            "text": self.text,
            "created": self.created
        }
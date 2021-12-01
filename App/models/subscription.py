from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref, relationship

# init db
db = SQLAlchemy()


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.Integer, db.ForeignKey('user.id'))
    topicID = db.Column(db.Integer, db.ForeignKey('topic.id'))
    created = db.Column(db.Datetime, nullable=False, default=datetime.now)
    status = db.Column(db.Integer, nullable=False, default=1)
    user = relationship("User", backref="subscription")
    topic = db.relationship("Topic", backref="subscription")
    

    def __repr__(self):
        return f"{self.userID}"


    def toDict(self):
        return {
            "userID": self.userID,
            "topicID": self.topicID
        }


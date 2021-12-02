from datetime import datetime
from . import db


class Subscription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="subscriptions")
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    topic = db.relationship("Topic", back_populates='subscriptions')
    created = db.Column(db.DateTime, nullable=False, default=datetime.now)
    status = db.Column(db.Integer, nullable=False, default=1)
    

    def __repr__(self):
        return f"{self.user_id}"


    def toDict(self):
        return {
            "userID": self.user_id,
            "topicID": self.topic_id
        }


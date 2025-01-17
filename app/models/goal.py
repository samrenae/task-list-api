from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goals")

    def to_dict(self):
        goal_dict = {
            "id": self.goal_id,
            "title": self.title
        }
        return goal_dict
    
    @classmethod
    def from_dict(cls, data_dict):
        new_goal = cls(title=data_dict["title"])
        return new_goal
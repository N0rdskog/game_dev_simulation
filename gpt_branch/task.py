from datetime import datetime

class Task:
    def __init__(self, description, assignee, due_date, priority):
        self.description = description
        self.assignee = assignee
        self.status = "Pending"
        self.due_date = due_date
        self.priority = priority

    def update_status(self, new_status):
        self.status = new_status

    def to_dict(self):
        return {
            "description": self.description,
            "assignee": self.assignee.name,
            "status": self.status,
            "due_date": self.due_date.strftime('%Y-%m-%d'),
            "priority": self.priority
        }
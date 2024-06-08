import random
from task import Task

class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.performance = 0
        self.tasks = []
        self.performance_metrics = {
            "tasks_completed": 0,
            "quality_of_work": 0,
            "speed": 0
        }

    def send_message(self, receiver, message_type, content):
        message = {
            "sender": self.name,
            "receiver": receiver.name,
            "type": message_type,
            "content": content
        }
        return message

    def receive_message(self, message):
        print(f"{self.name} received a message from {message['sender']}: {message['type']} - {message['content']}")
        self.process_message(message)

    def process_message(self, message):
        pass  # To be implemented by subclasses

    def add_task(self, task):
        self.tasks.append(task)

    def update_task_status(self, task_description, new_status):
        for task in self.tasks:
            if task.description == task_description:
                task.update_status(new_status)
                if new_status == "Completed":
                    self.performance_metrics["tasks_completed"] += 1
                break

    def update_task_status(self, task_description, new_status):
        for task in self.tasks:
            if task.description == task_description:
                task.update_status(new_status)
                if new_status == "Completed":
                    self.performance_metrics["tasks_completed"] += 1
                break
            
    def report_task_status(self):
        for task in self.tasks:
            print(f"Task: {task.description}, Status: {task.status}, Due Date: {task.due_date}, Priority: {task.priority}")

    def update_performance(self, quality, speed):
        self.performance_metrics["quality_of_work"] += quality
        self.performance_metrics["speed"] += speed
from agents.agent import Agent
from task import Task

class Developer(Agent):
    def __init__(self, name):
        super().__init__(name, "Developer")

    def write_code(self, design_doc):
        return {"type": "game_code", "content": f"Code based on {design_doc['title']}"}

    def process_message(self, message):
        if message['type'] == 'design_document':
            print(f"{self.name} is writing code based on: {message['content']['title']}")
        elif message['type'] == 'task_assignment':
            task = Task(message['content']['description'], self, message['content']['due_date'], message['content']['priority'])
            self.add_task(task)
            print(f"{self.name} received a new task: {task.description}")
        elif message['type'] == 'task_status':
            print(f"Task status update: {message['content']}")
        elif message['type'] == 'performance_update':
            quality, speed = message['content']['quality'], message['content']['speed']
            self.update_performance(quality, speed)
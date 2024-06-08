from agents.agent import Agent
from task import Task

class Artist(Agent):
    def __init__(self, name):
        super().__init__(name, "Artist")

    def create_assets(self):
        return {"type": "game_assets", "content": "Visual assets"}

    def process_message(self, message):
        if message['type'] == 'design_document':
            print(f"{self.name} is creating assets based on: {message['content']['title']}")
        elif message['type'] == 'task_assignment':
            task = Task(message['content']['description'], self, message['content']['due_date'], message['content']['priority'])
            self.add_task(task)
            print(f"{self.name} received a new task: {task.description}")
        elif message['type'] == 'task_status_request':
            self.report_task_status()
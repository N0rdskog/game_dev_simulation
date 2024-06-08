from agent import Agent
from task import Task

class GameDesigner(Agent):
    def __init__(self, name):
        super().__init__(name, "Game Designer")

    def create_design_document(self):
        return {
            "title": "Game Concept",
            "description": "A puzzle platformer with a unique time-rewind mechanic.",
            "details": "The player can rewind time to solve puzzles and navigate obstacles."
        }

    def create_task(self, description, assignee, due_date, priority):
        task = Task(description, assignee, due_date, priority)
        assignee.add_task(task)
        return task

    def process_message(self, message):
        if message['type'] == 'feedback':
            print(f"{self.name} is processing feedback: {message['content']}")
        elif message['type'] == 'task_status':
            print(f"Task status update from {message['sender']}: {message['content']}")
        elif message['type'] == 'performance_update':
            quality, speed = message['content']['quality'], message['content']['speed']
            self.update_performance(quality, speed)

    def generate_tasks(self):
        tasks = [
            {"description": "Implement game mechanics", "role": "Developer", "priority": "High"},
            {"description": "Create visual assets", "role": "Artist", "priority": "High"},
            {"description": "Test game functionality", "role": "Tester", "priority": "High"}
        ]
        return tasks
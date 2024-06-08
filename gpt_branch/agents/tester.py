from agent import Agent
from task import Task

class Tester(Agent):
    def __init__(self, name):
        super().__init__(name, "Tester")

    def test_game(self, game_code, game_assets):
        return {"type": "test_report", "content": f"Test report for {game_code['content']} with {game_assets['content']}"}

    def process_message(self, message):
        if message['type'] == 'game_code':
            print(f"{self.name} is testing the game code: {message['content']}")
        elif message['type'] == 'game_assets':
            print(f"{self.name} is testing the game assets: {message['content']}")
        elif message['type'] == 'task_assignment':
            task = Task(message['content']['description'], self, message['content']['due_date'], message['content']['priority'])
            self.add_task(task)
            print(f"{self.name} received a new task: {task.description}")
        elif message['type'] == 'task_status':
            print(f"Task status update: {message['content']}")
        elif message['type'] == 'performance_update':
            quality, speed = message['content']['quality'], message['content']['speed']
            self.update_performance(quality, speed)
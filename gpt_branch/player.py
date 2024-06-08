from agent import Agent
from task import Task
from game_interface import GameInterface
import random

class Player(Agent):
    def __init__(self, name):
        super().__init__(name, "Player")
        self.skill_level = 0

    def play_game(self, game: GameInterface):
        game.reset()
        game_over = False
        while not game_over:
            event = self.get_next_event(game)
            game.handle_event(event)
            game.update()
            if game.is_over():
                game_over = True
        if game.get_winner() == 1:
            self.skill_level += 1
        return {"type": "player_feedback", "content": f"Played game with result: {game.get_winner()}"}

    def get_next_event(self, game: GameInterface):
        available_moves = self.get_available_moves(game)
        move = random.choice(available_moves)
        return (move[0], move[1], 1)  # Assuming player is always 1 for simplicity

    def get_available_moves(self, game: GameInterface):
        state = game.get_state()
        moves = []
        for row in range(state.shape[0]):
            for col in range(state.shape[1]):
                if state[row][col] == 0:
                    moves.append((row, col))
        return moves

    def train(self, game: GameInterface, iterations=100):
        for _ in range(iterations):
            self.play_game(game)

    def process_message(self, message):
        if message['type'] == 'game_code':
            print(f"{self.name} is playing the game: {message['content']}")
        elif message['type'] == 'game_assets':
            print(f"{self.name} is analyzing the assets: {message['content']}")
        elif message['type'] == 'task_assignment':
            task = Task(message['content']['description'], self, message['content']['due_date'], message['content']['priority'])
            self.add_task(task)
            print(f"{self.name} received a new task: {task.description}")
        elif message['type'] == 'task_status_request':
            self.report_task_status()
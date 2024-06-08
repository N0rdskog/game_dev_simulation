import random
from agent import Agent
from task import Task
from tic_tac_toe import TicTacToe

class Player(Agent):
    def __init__(self, name):
        super().__init__(name, "Player")
        self.skill_level = 0

    def play_game(self, game, letter):
        game_over = False
        while not game_over:
            if game.num_empty_squares() == 0:
                game_over = True
                break
            if letter == 'X':
                move = self.get_best_move(game, letter)
                game.make_move(move, letter)
                if game.current_winner:
                    game_over = True
                    break
                letter = 'O'
            else:
                move = random.choice(game.available_moves())
                game.make_move(move, letter)
                if game.current_winner:
                    game_over = True
                    break
                letter = 'X'
        if game.current_winner == 'X':
            self.skill_level += 1
        return {"type": "player_feedback", "content": f"Played game with result: {game.current_winner}"}

    def train(self, iterations=100):
        for _ in range(iterations):
            game = TicTacToe()
            self.play_game(game, 'X')

    def get_best_move(self, game, letter):
        best_score = -float('inf')
        best_move = None
        for possible_move in game.available_moves():
            game.make_move(possible_move, letter)
            if game.current_winner:
                score = 1
            else:
                score = 0
            game.board[possible_move] = ' '
            if score > best_score:
                best_score = score
                best_move = possible_move
        return best_move

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
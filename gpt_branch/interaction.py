import json
import random
from datetime import datetime, timedelta
from game_designer import GameDesigner
from developer import Developer
from artist import Artist
from tester import Tester
from player import Player
from tic_tac_toe import TicTacToe

class InteractionManager:
    def __init__(self):
        self.agents = {
            "designer": GameDesigner("Designer_1"),
            "developer": Developer("Developer_1"),
            "artist": Artist("Artist_1"),
            "tester": Tester("Tester_1"),
            "player": Player("Player_1")
        }

    def run_interaction(self):
        designer = self.agents["designer"]
        developer = self.agents["developer"]
        artist = self.agents["artist"]
        tester = self.agents["tester"]
        player = self.agents["player"]

        # Designer creates a design document and sends it to the Developer and Artist
        design_doc = designer.create_design_document()
        message_to_dev = designer.send_message(developer, "design_document", design_doc)
        message_to_artist = designer.send_message(artist, "design_document", design_doc)

        developer.receive_message(message_to_dev)
        artist.receive_message(message_to_artist)

        # Designer generates dynamic tasks
        tasks = designer.generate_tasks()
        due_date = datetime.now() + timedelta(days=7)
        for task_info in tasks:
            task_description = task_info["description"]
            task_role = task_info["role"]
            task_priority = task_info["priority"]

            if task_role == "Developer":
                task_to_dev = designer.create_task(task_description, developer, due_date, task_priority)
                message_to_dev_task = designer.send_message(developer, "task_assignment", task_to_dev.to_dict())
                developer.receive_message(message_to_dev_task)
            elif task_role == "Artist":
                task_to_artist = designer.create_task(task_description, artist, due_date, task_priority)
                message_to_artist_task = designer.send_message(artist, "task_assignment", task_to_artist.to_dict())
                artist.receive_message(message_to_artist_task)
            elif task_role == "Tester":
                task_to_tester = designer.create_task(task_description, tester, due_date, task_priority)
                message_to_tester_task = designer.send_message(tester, "task_assignment", task_to_tester.to_dict())
                tester.receive_message(message_to_tester_task)

        # Agents work on their tasks
        developer.update_task_status("Implement game mechanics", "In Progress")
        artist.update_task_status("Create visual assets", "In Progress")

        # Developer reports task status to Designer
        message_task_status_dev = developer.send_message(designer, "task_status", "Implement game mechanics: In Progress")
        designer.receive_message(message_task_status_dev)

        # Developer writes code and sends it to the Tester
        game_code = developer.write_code(design_doc)
        message_to_tester = developer.send_message(tester, "game_code", game_code)

        # Mark Developer task as completed
        developer.update_task_status("Implement game mechanics", "Completed")
        message_task_status_dev_completed = developer.send_message(designer, "task_status", "Implement game mechanics: Completed")
        designer.receive_message(message_task_status_dev_completed)

        tester.receive_message(message_to_tester)

        # Artist creates assets and sends them to the Tester
        game_assets = artist.create_assets()
        message_to_tester_assets = artist.send_message(tester, "game_assets", game_assets)

        # Mark Artist task as completed
        artist.update_task_status("Create visual assets", "Completed")
        message_task_status_artist_completed = artist.send_message(designer, "task_status", "Create visual assets: Completed")
        designer.receive_message(message_task_status_artist_completed)

        tester.receive_message(message_to_tester_assets)

        # Tester tests the game and provides feedback
        test_report = tester.test_game(game_code, game_assets)
        print(json.dumps(test_report, indent=2))

        # Player plays the game and provides feedback
        game = TicTacToe()  # Initialize TicTacToe game
        player_feedback = player.play_game(game)
        print(json.dumps(player_feedback, indent=2))

        # Player trains to improve skills
        player.train(game)

        # Performance metrics update
        self.update_performance_metrics()

    def update_performance_metrics(self):
        for role, agent in self.agents.items():
            agent.update_performance(quality=random.randint(1, 5), speed=random.randint(1, 5))
            print(f"{agent.name} ({agent.role}) Performance Metrics: {agent.performance_metrics}")
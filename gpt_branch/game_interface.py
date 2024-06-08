from abc import ABC, abstractmethod

class GameInterface(ABC):
    @abstractmethod
    def reset(self):
        """Reset the game to its initial state."""
        pass

    @abstractmethod
    def handle_event(self, event):
        """Handle a game event."""
        pass

    @abstractmethod
    def update(self):
        """Update the game state."""
        pass

    @abstractmethod
    def get_state(self):
        """Return the current state of the game."""
        pass

    @abstractmethod
    def is_over(self):
        """Check if the game is over."""
        pass

    @abstractmethod
    def get_winner(self):
        """Return the winner of the game, if any."""
        pass
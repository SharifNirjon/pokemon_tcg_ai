from src.search.mcts import MCTS


class MCTSPolicy:
    def __init__(self, num_simulations=100):
        self.mcts = MCTS(num_simulations=num_simulations)

    def select_action(self, observation):
        return self.mcts.search(observation)

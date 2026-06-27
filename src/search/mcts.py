import math
import random


class MCTSNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.children = []
        self.visits = 0
        self.value = 0.0

    def ucb_score(self, c=1.41):
        if self.visits == 0:
            return float("inf")
        return self.value / self.visits + c * math.sqrt(
            math.log(self.parent.visits) / self.visits
        )


class MCTS:
    def __init__(self, num_simulations=100):
        self.num_simulations = num_simulations

    def search(self, observation):
        root = MCTSNode(state=observation)
        for _ in range(self.num_simulations):
            node = self._select(root)
            result = self._simulate(node.state)
            self._backpropagate(node, result)
        best = max(root.children, key=lambda n: n.visits, default=None)
        return best.action if best else None

    def _select(self, node):
        while node.children:
            node = max(node.children, key=lambda n: n.ucb_score())
        return node

    def _simulate(self, state):
        # TODO: implement rollout using game rules
        return random.random()

    def _backpropagate(self, node, result):
        while node:
            node.visits += 1
            node.value += result
            node = node.parent

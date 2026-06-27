from src.policies.heuristic_policy import HeuristicPolicy


class Agent:
    def __init__(self, policy=None):
        self.policy = policy or HeuristicPolicy()

    def act(self, observation):
        return self.policy.select_action(observation)

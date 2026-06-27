import random


class RandomPolicy:
    def select_action(self, observation):
        actions = observation.get("legal_actions", [])
        return random.choice(actions) if actions else None

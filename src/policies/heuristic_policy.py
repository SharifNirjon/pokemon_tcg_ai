class HeuristicPolicy:
    def select_action(self, observation):
        actions = observation.get("legal_actions", [])
        if not actions:
            return None
        # TODO: implement heuristic action selection
        return actions[0]

def get_legal_actions(observation):
    return observation.get("legal_actions", [])


def is_terminal(observation):
    return observation.get("done", False)


def get_reward(observation):
    return observation.get("reward", 0.0)

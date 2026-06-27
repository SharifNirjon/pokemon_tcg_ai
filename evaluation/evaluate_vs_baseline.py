"""Evaluate the main agent against random and heuristic baselines."""
from src.agent import Agent
from src.policies.random_policy import RandomPolicy
from src.policies.heuristic_policy import HeuristicPolicy


def evaluate(num_games=200):
    agent = Agent()
    baselines = {
        "random": Agent(policy=RandomPolicy()),
        "heuristic": Agent(policy=HeuristicPolicy()),
    }
    for name, baseline in baselines.items():
        wins = 0
        # TODO: implement game loop
        print(f"vs {name}: {wins / num_games:.2%} win rate")


if __name__ == "__main__":
    evaluate()

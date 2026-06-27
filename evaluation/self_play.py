"""Run the agent against itself and record results."""
from src.agent import Agent


def run(num_games=100):
    agent = Agent()
    wins = 0
    for _ in range(num_games):
        # TODO: implement game loop
        pass
    print(f"Win rate: {wins / num_games:.2%}")


if __name__ == "__main__":
    run()

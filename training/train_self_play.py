"""Self-play training loop."""
import yaml
from src.agent import Agent


def train(config_path="training/config/train_config.yaml"):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    agent = Agent()
    # TODO: implement self-play loop using config
    print(f"Starting self-play training for {config['num_episodes']} episodes")


if __name__ == "__main__":
    train()

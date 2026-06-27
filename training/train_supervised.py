"""Supervised training from recorded game logs."""
import yaml


def train(config_path="training/config/train_config.yaml"):
    with open(config_path) as f:
        config = yaml.safe_load(f)

    # TODO: load dataset, define model, run training loop
    print(f"Starting supervised training with batch size {config['batch_size']}")


if __name__ == "__main__":
    train()

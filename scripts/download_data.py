"""Download competition data into data/."""
import os

DATA_URL = ""  # TODO: fill in the competition data URL


def download():
    os.makedirs("data/cards", exist_ok=True)
    os.makedirs("data/decks", exist_ok=True)
    # TODO: implement download logic
    print("Data downloaded to data/")


if __name__ == "__main__":
    download()

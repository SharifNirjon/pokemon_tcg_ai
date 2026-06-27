from src.utils.game_utils import get_legal_actions, is_terminal, get_reward


def test_get_legal_actions():
    obs = {"legal_actions": ["attack", "pass"]}
    assert get_legal_actions(obs) == ["attack", "pass"]


def test_is_terminal():
    assert is_terminal({"done": True}) is True
    assert is_terminal({"done": False}) is False


def test_get_reward():
    assert get_reward({"reward": 1.0}) == 1.0
    assert get_reward({}) == 0.0

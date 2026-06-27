import pytest
from src.policies.random_policy import RandomPolicy
from src.policies.heuristic_policy import HeuristicPolicy


@pytest.fixture
def obs():
    return {"legal_actions": ["attack", "retreat"]}


def test_random_policy(obs):
    policy = RandomPolicy()
    action = policy.select_action(obs)
    assert action in obs["legal_actions"]


def test_heuristic_policy(obs):
    policy = HeuristicPolicy()
    action = policy.select_action(obs)
    assert action in obs["legal_actions"]


def test_policies_handle_empty_actions():
    empty_obs = {"legal_actions": []}
    assert RandomPolicy().select_action(empty_obs) is None
    assert HeuristicPolicy().select_action(empty_obs) is None

import pytest
from src.agent import Agent


@pytest.fixture
def fake_obs():
    return {"legal_actions": ["attack", "retreat", "pass"], "done": False, "reward": 0}


def test_agent_returns_action(fake_obs):
    agent = Agent()
    action = agent.act(fake_obs)
    assert action in fake_obs["legal_actions"]

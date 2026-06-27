"""
COMPETITION ENTRY — do not import training or evaluation code here.
"""
from src.agent import Agent


def get_action(observation):
    agent = Agent()
    return agent.act(observation)

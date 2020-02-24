
import logging

from rasa_core.agent import Agent
from rasa_core import config as policy_config
from rasa_core.policies.keras_policy import KerasPolicy
from rasa_core.policies.memoization import MemoizationPolicy

if __name__ =='__main__':
    logging.basicConfig(level='INFO')

    model_path = './models/dialogue'

    policies = policy_config.load("./policies.yml")

    agent = Agent('chat_domain.yml', policies = policies)

    training_data_file = agent.load_data('./stories.md')

    agent.train(
        training_data_file
    )
    agent.persist(model_path)
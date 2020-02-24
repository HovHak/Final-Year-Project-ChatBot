from rasa_core.channels.slack import SlackInput
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
import yaml
from rasa_core.utils import EndpointConfig


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/MyNLU')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhooks/slack/webhook")
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter, action_endpoint = action_endpoint)

input_channel = SlackInput( slack_token='xoxb-607403756646-603559674128-oIUzV7UMm3g81Nl3HrHzQF5b')

agent.handle_channels([input_channel], 5004, serve_forever=True)
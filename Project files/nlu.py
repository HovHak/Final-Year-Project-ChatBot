from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_nlu import config
#from rasa_nlu.converters import load_data
from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer, Interpreter, Metadata


def train (data, config_file, model_dir):
     training_data = load_data(data)
     configuration = config.load(config_file)
     trainer = Trainer(configuration)
     trainer.train(training_data)
     model_directory = trainer.persist(model_dir, fixed_model_name = 'MyNLU')

def run():
    interpreter = Interpreter.load('./models/nlu/default/MyNLU')
    print(interpreter.parse('what is the weather like in rome?'))

if __name__ == '__main__':
    train('./testData.json', './config.yml', './models/nlu')
    run()

#
# def run():
#     interpreter = Interpreter.load('./models/nlu/default/chat')
#     print(interpreter.parse('cancel my meeting'))
#     #print(interpreter.parse(u'What is the reivew for the movie Die Hard?'))
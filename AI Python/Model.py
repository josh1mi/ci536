from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class ChatbotModel:
    def __init__(self):
        self.bot = ChatBot(
            'Bicker',
            read_only=True,
            preprocessors=[
                'chatterbot.preprocessors.clean_whitespace',
                'chatterbot.preprocessors.convert_to_ascii'
            ],
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                {
                    'import_path': 'chatterbot.logic.BestMatch',
                    'default_response': 'I\'m sorry, I don\'t understand, please try asking something else',
                    'maximum_similarity_threshold': 0.90
                },
                {
                    'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                    'input_text': 'Log in',
                    'output_text': 'Please enter your customer number.'
                }
            ],
            database_uri='sqlite:///database.sqlite3'
        )

        self.trainer = ListTrainer(self.bot)

        # Training data
        self.train_data = [
            ['Help', 'Things you can ask me:'],
            ['I need help', 'What is the nature of the issue?'],
            ['I need a plumber', 'What is the nature of the issue?'],
            ['My boiler done broke', 'What is the nature of the issue?'],
            ['I\'m having heating issues', 'What is the nature of the issue?'],
            ['The drain is blocked', 'Have you tried using drain unblocker?'],
            ['Yes', 'Is the issue still persisting?'],
            ['There is no hot water', 'Have you tried restarting your boiler?'],
            ['Yes', 'Is the issue still persisting?'],
            ['My radiator is not working', 'Have you tried bleeding the radiator?'],
            ['Yes', 'Is the issue still persisting?'],
            ['YES', 'Are you a returning customer?'],
            ['Yes', 'Type \'Log in\' to continue'],
            ['YES', 'Are you a returning customer?'],
            ['No'],
            ['It\'s still broken', 'Are you a returning customer?']
        ]

        self.train_bot()

    def train_bot(self):
      for conversation in self.train_data:
        self.trainer.train(conversation)


    def get_response(self, user_input):
        return self.bot.get_response(user_input)

if __name__ == '__main__':
    bot = ChatbotModel()
    print('Hello, I\'m BickerBot. How may I help you today?')
    while True:
        try:
            user_input = input()
            bot_response = bot.get_response(user_input)
            print(bot_response)
        except (KeyboardInterrupt, EOFError, SystemExit):
            break

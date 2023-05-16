from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot(
        'Bicker',
        read_only=True,
        preprocessors=['chatterbot.preprocessors.clean_whitespace',
                       'chatterbot.preprocessors.convert_to_ascii'],
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                'import_path': 'chatterbot.logic.BestMatch',
                'default_response': 'I\'m sorry, I don\'t understand, please try asking something else',
                'maximum_similarity_threshold': 0.90
                # 'statement_comparison_function': 'chatterbot.comparisons.LevenshteinDistance',
                # 'response_selection_method': 'chatterbot.response_selection.get_first_response'
            },
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'Log in',
                'output_text': 'Please enter your customer number.'
            },
            {
                'import_path': 'chatterbot.logic.SpecificResponseAdapter',
                'input_text': 'help',
                'output_text': 'Here is a list of phrases to input:\nLog in\nMy boiler is broken\nI have a leak\nI\'m having heating issues'
            }
        ],
        # filters=[filters.get_recent_repeated_responses],
        database_uri='sqlite:///database.sqlite3'
    )

trainer = ListTrainer(bot)

trainer.train([
    'help',
    'Here is a list of phrases to input:',
    'Log in',
    'My boiler is broken',
    'I have a leak',
    'I\'m having heating issues',
])


trainer.train([
        'Help',
        'Things you can ask me:',
    ])

    #Train first stage of conversation
trainer.train([
        'I need help',
        'What is the nature of the issue?',
    ])
trainer.train([
        'I need a plumber',
        'What is the nature of the issue?',
    ])
trainer.train([
        'My boiler done broke',
        'What is the nature of the issue?',
    ])
trainer.train([
        'I\'m having heating issues',
        'What is the nature of the issue?',
    ])

    #Train second stage of conversation
trainer.train([
        'The drain is blocked',
        'Have you tried using drain unblocker?',
        'Yes',
        'Is the issue still persisting?',
    ])
trainer.train([
        'There is no hot water',
        'Have you tried restarting your boiler?',
        'Yes',
        'Is the issue still persisting?',
    ])
trainer.train([
        'My radiator is not working',
        'Have you tried bleeding the radiator?',
        'Yes',
        'Is the issue still persisting?',
    ])

    #Train third stage of conversation
trainer.train([
        'YES',
        'Are you a returning customer?',
        'Yes',
        'Type \'Log in\' to continue',
    ])
trainer.train([
        'YES',
        'Are you a returning customer?',
        'No',
    ])
trainer.train([
        'It\'s still broken',
        'Are you a returning customer?',
    ])

print('Hello, I\'m BickerBot. How may I help you today?')

while True:
    try:
        break
        bot_input = bot.get_response(input())
        print(bot_input)
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
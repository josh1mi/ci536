from chatterbot import ChatBot

bot = ChatBot(
    'Bicker',
    read_only=True,
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)

from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

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
    'What is your customer number?',
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
        bot_input = bot.get_response(input())
        print(bot_input)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break
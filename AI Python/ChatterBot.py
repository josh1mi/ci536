from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

chatbot = ChatBot("Chatpot")


exit_conditions = (":q", "quit", "exit")

while True:
    query = input("> ")

    if query in exit_conditions:
        break

    else:
        print(f"🪴 {chatbot.get_response(query)}")

import torchtext
from data import data

tokenizer = torchtext.data.utils.get_tokenizer("basic_english")

for item in data:
    question_tokens = tokenizer(item["question"])
    answer_tokens = tokenizer(item["answer"])
    print("Question Tokens:", question_tokens)
    print("Answer Tokens:", answer_tokens)

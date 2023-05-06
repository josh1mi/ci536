import torchtext
import torch

from data import data

tokenizer = torchtext.data.utils.get_tokenizer("basic_english")

# Build the vocabulary
vocab = torchtext.vocab.build_vocab_from_iterator(
    tokenizer(item["question"]) + tokenizer(item["answer"]) for item in data
)

for item in data:
    question_tokens = tokenizer(item["question"])
    answer_tokens = tokenizer(item["answer"])
    question_tokens = tokenizer(item["question"])
    answer_tokens = tokenizer(item["answer"])
    question_numerical = torch.tensor([vocab[token] for token in question_tokens])
    answer_numerical = torch.tensor([vocab[token] for token in answer_tokens])
    print("Question Tokens:", question_tokens)
    print("Question Numerical:", question_numerical)
    print("Answers Tokens:", answer_tokens)
    print("Answer Numerical:", answer_numerical)

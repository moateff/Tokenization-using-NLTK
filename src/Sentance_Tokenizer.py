import nltk
# nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

text = "Machine learning models are evolving rapidly, Tokenization is crucial in NLP tasks."

# Sentence Tokenization
sent_tokens = sent_tokenize(text)

print(f"\nSentance Tokens:\n{sent_tokens}\n")


# Sentence Tokenization (nltk): Tokenizing text into sentences is essential when working with
# paragraph-level data or summarization tasks.
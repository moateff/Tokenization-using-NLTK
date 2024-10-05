#pip install nltk

import nltk
# nltk.download('punkt_tab')

from nltk.tokenize import word_tokenize 
  
text = "Machine learning models are evolving rapidly. Tokenization is crucial in NLP tasks."

# Word Tokenization
word_tokens = word_tokenize(text)

print(f"\nWord Tokens:\n{word_tokens}\n")


# Word Tokenization (nltk): This method simply splits the text based on words and punctuation, 
# and is useful for basic applications.
# it is straightforward but doesn’t handle complex cases like contractions (e.g., "don’t").
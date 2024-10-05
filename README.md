# Tokenization using "NTLK":
In the context of machine learning, especially natural language processing (NLP), is the process of
breaking down a sequence of text (such as a sentence or paragraph) into smaller units called tokens.
Tokens can be words, sub words, or even characters, depending on the granularity. It’s a fundamental
step in preparing textual data for input into machine learning models, particularly those used for tasks 
such as text classification, translation, or sentiment analysis

# Types of Tokenization:
# 1. Sentence Tokenization:
This refers to breaking down text into its component sentences, which is particularly useful in tasks 
like document summarization or sentiment analysis at the sentence level. For example "Machine learning 
models are evolving rapidly. Tokenization is crucial in NLP tasks." would be tokenized into:
```
["Machine learning models are evolving rapidly. ", "Tokenization is crucial in NLP tasks. "]
```
# 2. Word Tokenization:
This involves splitting a text into its component words. For example, the sentence "Machine learning is 
fascinating" would be tokenized into:
```
["Machine", "learning", "is", "fascinating"]
```
# 3. Subword Tokenization:
In some cases, it's more effective to split words into smaller subword units. This is useful for handling 
rare words, as breaking them down into known subword parts allows the model to better generalize. 
Subword tokenization methods like Byte Pair Encoding (BPE) or WordPiece (used in BERT). For example, 
"unhappiness" could be tokenized as: 
```
["un", "##happy", "##ness"]
```
# 4. Character Tokenization:
In some cases, tokenizing at the character level can be beneficial, especially for tasks like text generation. 
For example, the word "machine" would be tokenized as: 
```
["m", "a", "c", "h", "i", "n", "e"]
```

# Named Entity & Noun Chunks using "spaCy":
# 1. Named Entity Recognition (NER):
Some common Named Entity labels you may encounter for named entities are:

PERSON: People, including fictional.
NORP: Nationalities or religious/political groups.
ORG: Organizations, companies, agencies.
GPE: Geopolitical entities (countries, cities).
MONEY: Monetary values.
DATE: Dates, periods.

spaCy automatically identifies entities like people, organizations, locations, monetary values, etc.
Each entity has a text (the entity itself) and a label_ (the type of the entity).

# 2. Noun Chunks:
Noun chunks are contiguous spans of tokens that form meaningful subjects or objects in the sentence.
spaCy identifies noun phrases (or noun chunks) in the text. doc.noun_chunks contains all the noun chunks.

Example Output
For the input text: "Apple is looking at buying U.K. startup for $1 billion. Elon Musk's Tesla is also interested."

Named Entities:
```
Apple ORG
U.K. GPE
$1 billion MONEY
Elon Musk PERSON
Tesla ORG
```
Noun Chunks:
```
Apple
U.K. startup
Elon Musk's Tesla
```


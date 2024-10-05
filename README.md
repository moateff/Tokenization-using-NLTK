# Tokenization:
In the context of machine learning, especially natural language processing (NLP), is the process of
breaking down a sequence of text (such as a sentence or paragraph) into smaller units called tokens.
Tokens can be words, sub words, or even characters, depending on the granularity. It’s a fundamental
step in preparing textual data for input into machine learning models, particularly those used for tasks 
such as text classification, translation, or sentiment analysis

# Types of Tokenization:
1. Sentence Tokenization:
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

import spacy

# Load the pre-trained spaCy model (English model)
nlp = spacy.load("en_core_web_sm")

# Sample text
text = "Apple is looking at buying U.K. startup for $1 billion. Elon Musk's Tesla is also interested."

# Process the text with spaCy
doc = nlp(text)

# Extract Named Entities (NER)
print("\nNamed Entities:")
for ent in doc.ents:
    print(ent.text, ent.label_)

# Extract Noun Chunks
print("\nNoun Chunks:")
for chunk in doc.noun_chunks:
    print(chunk.text)
print()

# Output Result 
# Named Entities:
# Apple ORG
# U.K. GPE
# $1 billion MONEY
# Elon Musk's PERSON
# Tesla ORG
#
# Noun Chunks:
# Apple
# U.K.
# Elon Musk's Tesla
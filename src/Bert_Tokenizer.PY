from transformers import BertTokenizer, BertModel

# Load BERT tokenizer and model
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

# Tokenize a sample text
text = "U.K. Hello, this is a test."
inputs = tokenizer(text, return_tensors="pt")
print(f"\nInput Tokens:\n{inputs}\n")

# Run the model
outputs = model(**inputs)
print(f"\nOutput Tokens:\n{outputs.last_hidden_state}\n")

# Subword Tokenization (BERT): BERT's tokenizer splits words into meaningful subword units.
# It helps handle words not present in the training vocabulary (out-of-vocabulary words).
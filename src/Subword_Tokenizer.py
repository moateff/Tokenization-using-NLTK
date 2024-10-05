# pip install transformers

from transformers import GPT2Tokenizer

# Load GPT-2 tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2', clean_up_tokenization_spaces = True)

# Input text
text = "Natural Language Processing is a fascinating field."

# Tokenize using GPT-2's BPE tokenizer
tokens = tokenizer.tokenize(text)

# Convert tokens to their respective IDs
token_ids = tokenizer.convert_tokens_to_ids(tokens)

print(f"\nBPE Tokens:\n{tokens}\n")
print(f"\nToken IDs:\n{token_ids}\n")


# Subword Tokenization (GPT-2 BPE): GPT-2 uses Byte Pair Encoding (BPE) to efficiently handle
# rare and unknown words by breaking them down into smaller subword units.
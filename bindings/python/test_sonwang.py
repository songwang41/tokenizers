from tokenizers_HF import CharBPETokenizer, ByteLevelBPETokenizer
vocab = "../../data/bart_large/vocab.json"
merges = "../../data/bart_large/merges.txt"
tokenizer = CharBPETokenizer(vocab, merges)

# And then encode:
encoded = tokenizer.encode("I can feel the magic, can you?")
print(encoded.ids)
print(encoded.tokens)
'''
>>> print(encoded.ids)
[3, 3245, 3, 33763, 3, 212, 3, 119, 18879, 3, 3, 3245, 3, 9839, 3, 3]
>>> print(encoded.tokens)
['<unk>', 'ca', '<unk>', 'fee', '<unk>', 'th', '<unk>', 'm', 'agi', '<unk>', '<unk>', 'ca', '<unk>', 'yo', '<unk>', '<unk>']
'''

tokenizer = ByteLevelBPETokenizer(vocab, merges)
encoded = tokenizer.encode("I can feel the magic, can you?")
print(encoded.ids)
print(encoded.tokens)

'''
>>> print(encoded.ids)
[100, 64, 619, 5, 8375, 6, 64, 47, 116]
>>> print(encoded.tokens)
['I', 'Ġcan', 'Ġfeel', 'Ġthe', 'Ġmagic', ',', 'Ġcan', 'Ġyou', '?']
'''
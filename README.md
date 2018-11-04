# Huffman Trees

This repository contains a simple Python implementation of Huffman trees. 

## Implementation Notes

- Constructs trees in an arbitrary base, inserting dummy symbols to be as efficient as possible
- `tests.py` tests that decoding an encoded message works properly and that the expected word length is within one bit of entropy by assembling a string of random symbols.
- `symbols.yaml` is a config file where you can put the symbols you want to encode (symbols should be single characters). The weights can be coefficients. They do not have to be probabilities; the code will normalize them into probabilities. You can also pick the word length for the test message there.

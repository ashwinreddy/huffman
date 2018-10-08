#!/usr/bin/env python
"""
Defines tests for Huffman encoding
"""

import unittest
import yaml
import huffman
import random
import copy
import math

def expected_word_length(tree, symbols, probability_map):
    expectation = 0
    for symbol in symbols:
        expectation += len(tree.encode(symbol)) * probability_map[symbol]
    return expectation

def entropy(probability_map, base):
    entropy = 0
    for _, prob in probability_map.items():
        entropy -= prob * math.log(prob, base)
    return entropy

class TestHuffmanTree(unittest.TestCase):
    def setUp(self):
        with open('symbols.yaml') as f:
            config = yaml.load(f)
        self.symbol_weights, self.base, self.test_message_length = config['symbol_weights'], config['base'], config['test_message_length']
        self.probability_map = copy.copy(self.symbol_weights)
        self.symbols = list(self.symbol_weights.keys())
        self.tree = huffman.buildHuffmanTree(self.symbol_weights, self.base)
    
    def test_encoding(self):
        symbols = random.choices(self.symbols, k = self.test_message_length)
        message = "".join(symbols)
        self.assertEqual(message, self.tree.decode_message(self.tree.encode_message(message)))
    
    def test_optimality(self):
        ewl = expected_word_length(self.tree, self.symbols, self.probability_map)
        its = entropy(self.probability_map, self.base)
        self.assertTrue(its <= ewl <= its + 1)

if __name__ == "__main__":
    unittest.main()
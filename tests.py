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
import numpy as np

def expected_word_length(tree, symbols, probability_map):
    expectation = 0
    for symbol in symbols:
        expectation += len(tree.encode(symbol)) * probability_map[symbol]
    return expectation

class TestHuffmanTree(unittest.TestCase):
    def setUp(self):
        with open('symbols.yaml') as f:
            config = yaml.load(f)
        self.symbol_weights, self.base, self.test_message_length = config['symbol_weights'], config['base'], config['test_message_length']
        
        self.probability_map    = huffman.ProbabilityMap(self.symbol_weights)
        self.symbols            = self.probability_map.keys()
        self.tree               = huffman.Weights(self.symbol_weights).buildTree(self.base)
    
    def test_encoding(self):
        """
        Tests that decode-encode composition returns identity.
        """
        # Create a message of given length by stringing together randomly chosen symbols
        message = "".join(random.choices(self.symbols, k = self.test_message_length))
        # assert that the message is returned when encoded and then decoded
        self.assertEqual(message, self.tree.decode_message(self.tree.encode_message(message)))
    
    def test_optimality(self):
        """
        Tests that Huffman coding is optimal (i.e. within 1 bit of entropy)
        """
        # compute expected word length
        ewl = expected_word_length(self.tree, self.symbols, self.probability_map)
        # compute entropy (result needs to be converted into the correct base)
        its = self.probability_map.entropy / np.log(self.base)
        # assert that the E[L] is within 1 bit of entropy
        self.assertTrue(its <= ewl <= its + 1)

if __name__ == "__main__":
    unittest.main()
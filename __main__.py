#!/usr/bin/env python
"""
Runs tests for Huffman Tree
"""

import huffman
import copy
import yaml

if __name__ == "__main__":
    with open('symbols.yaml') as f:
        config = yaml.load(f)
        symbol_weights, base, test_message_length = config['symbol_weights'], config['base'], config['test_message_length']
        probability_map = copy.copy(symbol_weights)
        symbols = list(symbol_weights.keys())
        tree = huffman.buildHuffmanTree(symbol_weights, base)
        print("Huffman Tree", tree)
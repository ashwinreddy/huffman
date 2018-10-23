#!/usr/bin/env python
"""
Defines Huffman Encoding Algorithm
"""
import numpy as np

argmin = lambda x: min(x, key=x.get)

class ProbabilityMap(object):
    def __init__(self, probs):
        total_weights = sum(probs.values())
        self.probs = { key : probs[key] / total_weights for key in probs }
    
    @property
    def entropy(self):
        p = np.array(list(self.probs.values()))
        return - p @ np.log(p)
    
    def keys(self):
        return list(self.probs.keys())
    
    def __getitem__(self, key):
        return self.probs[key]
    

class Weights(object):
    def __init__(self, weights):
        self.weights = weights
    
    def __len__(self):
        return len(self.weights)
    
    def pop_least_frequent_symbol(self):
        symbol = argmin(self.weights)
        weight = self.weights[symbol]
        del self.weights[symbol]
        return symbol, weight
    
    def buildTree(self, base):
        x = 1
        while ( len(self) - 1 ) % (base - 1) != 0:
            self.weights['null{}'.format(x)] = 0
            x += 1

        value = 0
        while len(self) > 1:
            stack = [None for _ in range(base)]
            total_weight = 0
            i = 0
            while i < base and len(self) != 0:
                last_symbol, last_weight = self.pop_least_frequent_symbol()
                stack[i] = last_symbol
                total_weight += last_weight
                i += 1
            new_symbol = HuffmanTree(stack, base=base)
            self.weights[new_symbol] = total_weight
            value += total_weight
        print("Weights add up to", value)
        
        [(tree, _ )] = self.weights.items()
        return tree

class HuffmanTree(object):
    """
    Defines a tree which may recursively include other trees. 
    The top node is capable of encoding and decoding messages.
    """

    def __init__(self, children: list, base: int = 2):
        """
        Create a tree with base nodes and initialize them with the children list
        """
        # check that the length of the list is equal to the "base" of the tree
        assert len(children) == base
        # initialize object properties
        self._children = children
        self._base = base
    

    def __str__(self):
        """
        Generates a user-readable string representing the tree
        """
        string_repr = ""
        # Loop through each children
        for idx, children in enumerate(self._children):
            # Generate a string for the children and add it to the 
            string_repr += str(children) + (", " if idx != len(self._children) - 1 else "") # Add a comma if there are more elements to come
        return "Tree({})".format(string_repr)
    
    def __repr__(self):
        return str(self)
    
    def encode(self, symbol):
        for instruction, branch in enumerate(self._children): 
            if type(branch) is HuffmanTree:
                    encoding = branch.encode(symbol)
                    if encoding:
                        return str(instruction) + branch.encode(symbol)
            elif branch == symbol:
                return str(instruction)
    
    def decode_message(self, instructions):
        instructions = [int(instruction) for instruction in instructions]
        message = ""
        tree = self
        for instruction in instructions:
            tree = tree._children[instruction]
            if type(tree) is str:
                message += tree
                tree = self
        return message
    
    def encode_message(self, message):
        return "".join([self.encode(char) for char in message])
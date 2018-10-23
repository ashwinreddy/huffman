#!/usr/bin/env python
"""
Defines Huffman Encoding Algorithm
"""

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
        
argmin = lambda x: min(x, key=x.get)

def pop_least_frequent_symbol(weights):
    symbol = argmin(weights)
    weight = weights[symbol]
    del weights[symbol]
    return symbol, weight

def buildHuffmanTree(weights, base):
    x=1
    while (len(weights)-1) % (base - 1) != 0:
        weights['null{}'.format(x)] = 0
        x+=1

    value = 0
    while len(weights) > 1:
        stack = [None for _ in range(base)]
        total_weight = 0
        i = 0
        while i < base and len(weights) != 0:
            last_symbol, last_weight = pop_least_frequent_symbol(weights)
            stack[i] = last_symbol
            total_weight += last_weight
            i += 1
        new_symbol = HuffmanTree(stack, base=base)
        weights[new_symbol] = total_weight
        value += total_weight
    print("Weights add up to", value)
    
    [(tree, _ )] = weights.items()
    return tree
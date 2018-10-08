class HuffmanTree(object):
    def __init__(self, children, base = 2):
        assert len(children) == base
        self._children = children
        self._base = base
    
    def __str__(self):
        string_repr = ""
        for idx, children in enumerate(self._children):
            string_repr += str(children) + (", " if idx != len(self._children) - 1 else "")
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
    
    [(tree, _ )] = weights.items()
    return tree

# for i in [2,3,4,5]:
#     tree = buildHuffmanTree(weights, i)
#     print(tree)
#     # print(tree.encode_message("12345"))
#     assert("5123312124" == tree.decode_message(tree.encode_message("5123312124")))
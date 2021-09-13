from dataclasses import dataclass


class AST(object):
    pass

@dataclass
class BinBoolFunc(AST):
    """
    Binary Bool Function
    """
    def __init__(self, left, op, right):
        self.left = left
        self.token = self.op = op
        self.right = right

@dataclass
class BoolNum(AST):
    """
    Bool number (0 or 1)
    """
    def __init__(self, token):
        self.token = token.type
        self.value = token.value

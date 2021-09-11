import enum

class TokenType(enum.Enum):
    T_BOOL = 0
    T_OR   = 1
    T_AND  = 2
    T_LPAR = 3
    T_RPAR = 4
    T_END  = 5


class Node:
    def __init__(self, token_type, value=None):
        self.token_type = token_type
        self.value = value
        self.children = []

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.value)
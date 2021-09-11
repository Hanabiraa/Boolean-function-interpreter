import re
import frontend.AST as AST


def create_word_tokens(expr):
    """
    Take raw expr after input and create tokens for AST
    :param expr: str
    :return: [[]]

    >>> create_word_tokens('a and (b xor x) or c')
    ['a', 'and', '(', 'b', 'xor', 'x', ')', 'or', 'c']
    """
    def complex_repl(char):
        """char: re.Math object """
        variants = {
            '(': '( ',
            ')': ' )'
        }
        return variants[char.group()]

    tokens = re.sub(r'[(]|[)]', complex_repl, expr).split()
    return tokens


def create_object_tokens(word_tokens):
    mappings = {
        'or' : AST.TokenType.T_OR,
        'and': AST.TokenType.T_AND,
        '('  : AST.TokenType.T_LPAR,
        ')'  : AST.TokenType.T_RPAR,
    }

    object_tokens = []
    for token in word_tokens:
        if token in mappings:
            token_type = mappings[token]
            token = AST.Node(token_type, value=token)
        else:
            token = AST.Node(AST.TokenType.T_BOOL, value=bool(int(token)))
        object_tokens.append(token)

    object_tokens.append(AST.Node(AST.TokenType.T_END))
    return object_tokens
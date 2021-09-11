import re


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


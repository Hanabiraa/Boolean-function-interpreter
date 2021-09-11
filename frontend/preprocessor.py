import re
import pandas as pd
from frontend.classes.Lexer import operator_table
from itertools import product


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


def truth_table_csv(tokens):
    """
    Create logical truth table in csv file in ./data
    :param tokens: [[str]]
    :return: None
    """
    vars = sorted(list({token for token in tokens if token not in operator_table}))
    vars_count = len(vars)
    truth_table = [i for i in product(['0', '1'], repeat=vars_count)]

    df = pd.DataFrame()
    for i in range(vars_count):
        srs = pd.Series([elem[i] for elem in truth_table], name=vars[i])
        df = pd.concat([df, srs], axis=1, ignore_index=False, names=vars)
    df.to_csv('./data/table.csv', index=False)


def create_list_of_tokens(tokens):
    """
    Create truth table and change all vars on different variants by rows in table
    :param tokens: [[str]]
    :return: [[str]]

    Example:
    >>> create_list_of_tokens(['(', 'x1', 'or', 'x2', ')'])
    [['(', '0', 'or', '0', ')'], ['(', '0', 'or', '1', ')'], ['(', '1', 'or', '0', ')'], ['(', '1', 'or', '1', ')']]
    """
    vars = sorted(list({token for token in tokens if token not in operator_table}))
    vars_count = len(vars)
    truth_table = [i for i in product(['0', '1'], repeat=vars_count)]

    lst_tokens = []
    for row in truth_table:
        logical_val = dict(zip(vars, row))
        tokens_ = [logical_val[token] if token in logical_val else token for token in tokens]
        lst_tokens.append(tokens_)

    return lst_tokens

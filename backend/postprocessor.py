from itertools import product
from frontend.classes.Lexer import operator_table
import pandas as pd


def create_truth_table_csv(tokens):
    """
    Create logical truth table in csv file in ./output_data
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
    df.to_csv('./output_data/table.csv', index=False)


def add_answers_to_csv(answers, expr='expression', visual=False):
    df = pd.read_csv('./output_data/table.csv')
    srs = pd.Series(answers, name='expr: '+expr)
    df = pd.concat([df, srs], axis=1, ignore_index=False)
    df.to_csv('./output_data/table.csv', index=False)

    if visual:
        print(df)

from itertools import product
from frontend.classes.Lexer import operator_table

import pandas as pd
import os


def create_truth_table(tokens, answers, expr='expression', visual=False, simple=False):
    """
    Creates a truth table and, depending on flags, saves and/or print them
    """
    if os.path.isfile('./output_data/table.csv'):
        os.remove('./output_data/table.csv')

    vars = sorted(list({token for token in tokens if token not in operator_table}))
    vars_count = len(vars)

    df = pd.DataFrame()
    if vars_count:
        truth_table_var = [i for i in product(['0', '1'], repeat=vars_count)]
        for i in range(vars_count):
            srs = pd.Series([elem[i] for elem in truth_table_var], name=vars[i])
            df = pd.concat([df, srs], axis=1, ignore_index=False, names=vars)

    srs = pd.Series(answers, name='expr: '+expr)
    df = pd.concat([df, srs], axis=1, ignore_index=False)

    if not simple:
        print('truth table saved in ./output_data/table.csv')
        df.to_csv('./output_data/table.csv', index=False)

    if visual or simple:
        print(df)

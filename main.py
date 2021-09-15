import argparse

from frontend.preprocessor import create_word_tokens, create_list_of_tokens
from frontend.classes.Lexer import Lexer
from frontend.classes.Parser import Parser
from frontend.debug import debug_func

from backend.classes.Interpreter import Interpreter
# from backend.postprocessor import create_truth_table_csv, add_answers_to_csv
from backend.postprocessor import create_truth_table


def main(debug=False, visual=False, simple=False, expr=''):
    # Intro
    raw_expr = input('prompt> ') if not len(expr) else expr

    # pre-processing
    word_tokens = create_word_tokens(raw_expr)
    semantic_tokens_lst = create_list_of_tokens(word_tokens)
    object_tokens_lst = [list(Lexer(tokens).generate_tokens()) for tokens in semantic_tokens_lst]

    # DEBUG
    if debug:
        debug_func(raw_expr, word_tokens, semantic_tokens_lst, object_tokens_lst)

    # creating AST and interpret them
    values = []
    for object_tokens in object_tokens_lst:
        parser = Parser(object_tokens)
        AST = parser.parse()
        values.append(Interpreter(AST).interpret())

    # if flag visual=True -> print pd.Dataframe to sys.stdout.write
    # create_truth_table_csv(word_tokens)
    # add_answers_to_csv(values, raw_expr, visual=visual)
    create_truth_table(word_tokens, values, raw_expr, visual=visual, simple=simple)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Bool complex function parser and calculator, save info in csv-file '
                                                 'in ./output_data')

    parser.add_argument('-v', '--visual', type=str, default=False, action=argparse.BooleanOptionalAction,
                        help='flag, if True - print pd.DataFrame with answers to sys.stdout.write'
                             ' and saves the file to the standard path ')
    parser.add_argument('-s', '--simple', type=str, default=False, action=argparse.BooleanOptionalAction,
                        help='flag, if True, it just outputs the answer without storing it anywhere')
    parser.add_argument('-e', '--expr', type=str, default='', help='You can enter an expression into this flag'
                                                                   ' if you don\'t want to do it through the main.py')
    parser.add_argument('-d', '--debug', type=str, default=False, action=argparse.BooleanOptionalAction,
                        help='flag, If True - outputs each change to the token array after the functions. Before the '
                             'Abstract Syntax Tree')

    args = parser.parse_args()
    main(debug=args.debug, visual=args.visual, simple=args.simple, expr=args.expr)

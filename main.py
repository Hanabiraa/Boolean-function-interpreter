from frontend.preprocessor import create_word_tokens, create_list_of_tokens, truth_table_csv
from frontend.classes.Lexer import Lexer
from frontend.debug import debug_func

if __name__ == '__main__':
    print('Hello, its math parser. Enter your expr:')
    # raw_expr = input()
    raw_expr = '(x1 or x2) or (x3 and x4)'

    # pre-processing for lexer
    word_tokens = create_word_tokens(raw_expr)

    # create csv file with truth table
    truth_table_csv(word_tokens)

    # create list of different tokens-word (different logical vars)
    semantic_tokens_lst = create_list_of_tokens(word_tokens)

    # object-tokens with logging after lexer
    object_tokens_lst = [list(Lexer(tokens).generate_tokens()) for tokens in semantic_tokens_lst]

    # DEBUG
    debug_func(raw_expr, word_tokens, semantic_tokens_lst, object_tokens_lst)



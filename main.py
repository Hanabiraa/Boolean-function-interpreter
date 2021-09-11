from frontend.preprocessor import  create_word_tokens
from frontend.classes.Lexer import Lexer
if __name__ == '__main__':
    print('Hello, its math parser. Enter your expr:')
    # raw_expr = input()
    raw_expr = '0 or 1 and 0'
    print('your expr: {}'.format(raw_expr))

    # pre-processing for lexer
    word_tokens = create_word_tokens(raw_expr)
    print('simple tokens:', word_tokens, sep='\n')

    # object-tokens with logging after lexer
    object_tokens = Lexer(word_tokens).generate_tokens()
    print('object tokens:', list(object_tokens), sep='\n')
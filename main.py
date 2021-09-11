from frontend.lexical_analysis import create_word_tokens, create_object_tokens
from frontend.parser import *
import frontend.AST as AST
from backend.compute import *


if __name__ == '__main__':
    print('Hello, its math parser. Enter your expr:')
    # raw_expr = input()
    raw_expr = '0 and 1 or 1'
    print('your expr: {}'.format(raw_expr))

    word_tokens   = create_word_tokens(raw_expr)
    print(word_tokens)

    object_tokens = create_object_tokens(word_tokens)
    print(object_tokens)

    ast = parse_e(object_tokens)
    match(object_tokens, AST.TokenType.T_END)
    print(ast)

    result = compute(ast)
    print(result)




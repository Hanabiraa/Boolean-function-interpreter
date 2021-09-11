from frontend.preprocessor import create_word_tokens
from frontend.classes.Lexer import Lexer
from frontend.classes.Parser import Parser
from backend.Interpreter import Interpreter

if __name__ == '__main__':
    print('Hello, its math parser. Enter your expr:')
    # raw_expr = input()
    raw_expr = '0 or 1 and 0'
    print('your expr: {}'.format(raw_expr))

    tokens = create_word_tokens(raw_expr)
    print(tokens)

    lexer = Lexer(tokens)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    print('its 1')
    result = interpreter.interpret()
    print(result)

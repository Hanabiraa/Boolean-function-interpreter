from frontend.classes.Token import TokenType, Token

# global dict
operator_table = {
            '0': 0,
            '1': 1,
            'eqv': TokenType.EQV,
            'le': TokenType.LE,
            'ge': TokenType.GE,
            'or': TokenType.OR,
            'and': TokenType.AND,
            '(': TokenType.LPAREN,
            ')': TokenType.RPAREN,
            'not': TokenType.NOT,
}


class Lexer:
    """
    Create object-tokens for parser
    """
    def __init__(self, word_tokens):
        self.tokens = iter(word_tokens)
        self.current_token = None
        self.next_token()

    def next_token(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def generate_tokens(self):
        global operator_table
        while self.current_token is not None:
            if self.current_token in {'0', '1'}:
                yield Token(TokenType.BOOL_VAR, operator_table[self.current_token])
                self.next_token()
            elif self.current_token in operator_table:
                yield Token(operator_table[self.current_token])
                self.next_token()
            else:
                raise Exception('Illegal token! {}'.format(self.current_token))

from frontend.classes.Token import TokenType, Token


class Lexer:
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
        operator_table = {
            'or': TokenType.OR,
            'and': TokenType.AND,
            'not': TokenType.NOT,
        }

        while self.current_token is not None:
            if self.current_token not in operator_table:
                yield Token(TokenType.BOOL_VAR)
                self.next_token()
            elif self.current_token in operator_table:
                yield Token(operator_table[self.current_token])
                self.next_token()
            else:
                raise Exception('Illegal token! {}'.format(self.current_token))

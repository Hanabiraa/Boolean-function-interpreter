from frontend.classes.Token import TokenType, Token
import operator


class Lexer(object):
    def __init__(self, tokens):
        """
        initialize lexer by tokens
        :param tokens: list(list(str()))

        pos - for indexing into self.tokens
        """
        self.tokens = tokens
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        """
        create one object token
        """
        if self.pos > len(self.tokens) - 1:
            return Token(TokenType.T_END, None)
        else:
            token = self.tokens[self.pos]
            self.pos = self.pos + 1

        token_table_operation_type = {
            '0':Token(TokenType.T_BOOL, False),
            '1':Token(TokenType.T_OR, True),
            'or': Token(TokenType.T_OR, TokenType.T_OR),
            'and': Token(TokenType.T_AND, TokenType.T_AND),
            '(': Token(TokenType.T_LPARENT, TokenType.T_LPARENT),
            ')': Token(TokenType.T_RPARENT, TokenType.T_RPARENT),
        }
        object_token = token_table_operation_type[token] if token in token_table_operation_type\
            else Token(TokenType.T_BOOL, token)

        return object_token

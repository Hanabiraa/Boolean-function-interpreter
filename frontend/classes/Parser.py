from frontend.classes.Token import TokenType
from frontend.classes.AST import BoolVar, BinOp


class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def set_curr_token(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        """factor : TokenType.T_BOOL | LPAREN expr RPAREN"""
        token = self.current_token
        if token.type == TokenType.T_BOOL:
            self.set_curr_token(TokenType.T_BOOL)
            return BoolVar(token)
        elif token.type == TokenType.T_LPARENT:
            self.set_curr_token(TokenType.T_LPARENT)
            node = self.expr()
            self.set_curr_token(TokenType.T_RPARENT)
            return node

    def term(self):
        """term : factor ((T_AND) factor)*"""
        node = self.factor()

        while self.current_token.type == TokenType.T_AND:
            token = self.current_token
            if token.type == TokenType.T_AND:
                self.set_curr_token(TokenType.T_AND)

            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr   : term ((T_OR) term)*
        term   : factor ((T_MUL) factor)*
        factor : T_BOOL | T_LPARENT expr T_RPARENT
        """
        node = self.term()

        while self.current_token.type == TokenType.T_OR:
            token = self.current_token
            if token.type == TokenType.T_OR:
                self.set_curr_token(TokenType.T_OR)

            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()

from frontend.classes.Token import Token, TokenType
from frontend.classes.AST import BinBoolFunc, BoolNum, BoolNegation


class Parser(object):
    """
    Create AST
    """
    def __init__(self, obj_tokens):
        self.tokens = iter(obj_tokens)
        self.current_token = None
        self.next_token()

    def next_token(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = Token(TokenType.EOF)

    def factor(self):
        token = self.current_token
        if token.type == TokenType.BOOL_VAR:
            self.next_token()
            return BoolNum(token)
        elif token.type == TokenType.NOT:
            self.next_token()
            node = BoolNegation(token, self.factor())
            return node
        elif token.type == TokenType.LPAREN:
            self.next_token()
            node = self.expr()
            self.next_token()
            return node

    def term(self):
        node = self.factor()

        while self.current_token.type in {TokenType.AND}:
            token = self.current_token
            if token.type == TokenType.AND:
                self.next_token()
            # elif token.type == DIV:
            #     self.eat(DIV)

            node = BinBoolFunc(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        node = self.term()

        while self.current_token.type in {TokenType.OR}:
            token = self.current_token
            if token.type == TokenType.OR:
                self.next_token()
            # elif token.type == MINUS:
            #     self.eat(MINUS)

            node = BinBoolFunc(left=node, op=token, right=self.term())

        return node

    def parse(self):
        return self.expr()

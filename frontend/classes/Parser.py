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
        """
        bool number, bool NOT, ()
        """
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
        """
        bool AND
        """
        node = self.factor()

        while self.current_token.type in {TokenType.AND}:
            token = self.current_token
            if token.type == TokenType.AND:
                self.next_token()

            node = BinBoolFunc(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        Bool OR
        """
        node = self.term()

        while self.current_token.type in {TokenType.OR}:
            token = self.current_token
            if token.type == TokenType.OR:
                self.next_token()

            node = BinBoolFunc(left=node, op=token, right=self.term())

        return node

    def logical_impl(self):
        """
        represent IMPLICATION
        """
        node = self.expr()

        while self.current_token.type in {TokenType.LE, TokenType.GE}:
            token = self.current_token
            if token.type == TokenType.LE:
                self.next_token()
            elif token.type == TokenType.GE:
                self.next_token()

            node = BinBoolFunc(left=node, op=token, right=self.expr())

        return node
    def logical_eqv(self):
        """
        represent low level: equivalency (EQV)
        """
        node = self.logical_impl()

        while self.current_token.type in {TokenType.EQV}:
            token = self.current_token
            if token.type == TokenType.EQV:
                self.next_token()

            node = BinBoolFunc(left=node, op=token, right=self.logical_impl())

        return node

    def parse(self):
        return self.logical_eqv()

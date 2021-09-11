import enum


class TokenType(enum.Enum):
    T_BOOL, T_OR, T_AND, T_LPARENT, T_RPARENT, T_END = range(0, 6)


class Token(object):
    def __init__(self, token_type, token_value):
        """
        :param token_type: TokenType
        :param token_value: str or int or bool
        """
        self.type = token_type
        self.value = token_value

    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        """
        >>> print(Token(T_BOOL, '0'))
            Token(T_BOOL, '0')
        """
        return self.__str__()


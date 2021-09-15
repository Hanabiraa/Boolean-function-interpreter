from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
	BOOL_VAR, GE, LE, EQV, OR, XOR, NOR, AND, NAND, LPAREN, RPAREN, NOT, EOF = range(13)


@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value is not None else "")

from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
	BOOL_VAR = 0,
	GE = 1,
	LE = 2,
	EQV = 3,
	OR = 4,
	AND = 5,
	LPAREN = 6,
	RPAREN = 7,
	NOT = 8,
	EOF = 9


@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value is not None else "")
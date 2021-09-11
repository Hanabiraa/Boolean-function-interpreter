from enum import Enum
from dataclasses import dataclass


class TokenType(Enum):
	BOOL_VAR  = 0
	OR        = 1
	AND       = 2
	NOT  	  = 3
	LPAREN    = 4
	RPAREN    = 5


@dataclass
class Token:
	type: TokenType
	value: any = None

	def __repr__(self):
		return self.type.name + (f":{self.value}" if self.value is not None else "")
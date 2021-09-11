import sys
import operator
import frontend.parser as parser
import frontend.AST as AST


operations = {
    AST.TokenType.T_OR: operator.or_,
    AST.TokenType.T_AND: operator.and_,

}


def compute(node):
    if node.token_type == AST.TokenType.T_BOOL:
        return node.value
    left_result = compute(node.children[0])
    right_result = compute(node.children[1])
    operation = operations[node.token_type]
    return operation(left_result, right_result)
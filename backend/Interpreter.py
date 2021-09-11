from frontend.classes.Token import TokenType
from frontend.classes.Parser import *
from operator import or_, and_


class NodeVisitor(object):
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        print('its 3')
        return visitor(node)

    def generic_visit(self, node):
        print('its 5')
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    def __init__(self, parser):
        self.parser = parser

    def visit_BinOp(self, node):
        print('its 4')
        if node.op.type == TokenType.T_OR:
            return self.visit(node.left) or self.visit(node.right)
        elif node.op.type == TokenType.T_AND:
            return self.visit(node.left) and self.visit(node.right)

    def visit_BoolVar(self, node):
        return node.value

    def interpret(self):
        tree = self.parser.parse()
        print('its 2')
        return self.visit(tree)
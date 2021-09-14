from frontend.classes.Token import TokenType


class NodeVisitor(object):
    """
    visit node
    """
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise Exception('No visit_{} method'.format(type(node).__name__))


class Interpreter(NodeVisitor):
    """
    Interpreter for calculate answer for AST (which is bool complex function)
    """
    def __init__(self, AST_head):
        self.head_node = AST_head

    def visit_BoolNegation(self, node):
        """
        Represent negation
        """
        return int(not(self.visit(node.expr)))

    def visit_BinBoolFunc(self, node):
        """
        Represent operand
        """
        if node.op.type == TokenType.AND:
            return self.visit(node.left) and self.visit(node.right)
        elif node.op.type == TokenType.OR:
            return self.visit(node.left) or self.visit(node.right)
        elif node.op.type == TokenType.EQV:
            return int(self.visit(node.left) is self.visit(node.right))
        elif node.op.type == TokenType.LE:
            return int(not self.visit(node.left) or self.visit(node.right))
        elif node.op.type == TokenType.GE:
            return int(self.visit(node.left) or not self.visit(node.right))

    def visit_BoolNum(self, node):
        """
        Represent value
        """
        return node.value

    def interpret(self):
        return self.visit(self.head_node)
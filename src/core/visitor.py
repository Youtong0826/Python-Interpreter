from core._ast_ import ASTNode, BinaryOperatorNode
from core._token import Token, Operator, DataType

class NodeVisitor:
    def visit(self, node: ASTNode):
        if isinstance(node, BinaryOperatorNode):
            left: Token = self.visit(node.left)
            right: Token = self.visit(node.right)
            
            match node.token.type:
                case Operator.ADD:
                    return Token(DataType.NUM, left.value + right.value)
                
                case Operator.SUB:
                    return Token(DataType.NUM, left.value - right.value)
                
                case Operator.MUL:
                    return Token(DataType.NUM, left.value * right.value)
                
                case Operator.DIV:
                    return Token(DataType.NUM, left.value // right.value)
            
        return node.token


from _token import Token
from typing import Any

class ASTNode:
    def __init__(self, token: Token) -> None: 
        self.token = token
    
class DataNode(ASTNode):
    def __init__(self, token: Token, value: Any) -> None: 
        super().__init__(token)
        self.value = value
    
class BinaryOperatorNode(ASTNode):
    def __init__(self, token: Token, left: ASTNode, right: ASTNode) -> None: 
        super().__init__(token)
        self.left = left
        self.right = right
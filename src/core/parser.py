from core._ast_ import DataNode, BinaryOperatorNode
from core._token import DataType, Operator
from core.lexer import Lexer
from typing import Union

class Parser:
    def __init__(self, lexer: Lexer) -> None:
        self.__lexer = lexer
        self.__token = lexer.next()
        
    def __throw(self, type: Union[DataType, Operator]):
        if self.__token.type == type:
            self.__token = self.__lexer.next()
            
        else:
            raise TypeError(f"Expected token {type}, but got {self.__token.type}")
    
    def __factor(self):
        match self.__token.type:
            case DataType.NUM:
                node = DataNode(self.__token, int(self.__token.value))
                self.__throw(DataType.NUM)
                return node
        
        raise SyntaxError("Invalid syntax")
        
    def __term(self):
        node = self.__factor()
        while self.__token and self.__token.type in [Operator.MUL, Operator.DIV]:
            op = self.__token
            self.__throw(op.type)
            node = BinaryOperatorNode(op, node, self.__factor())
            
        return node
        
    def __expr(self):
        node = self.__term()
        while self.__token and self.__token.type in [Operator.ADD, Operator.SUB]:
            op = self.__token
            self.__throw(op.type)
            node = BinaryOperatorNode(op, node, self.__term())
            
        return node
            
    def parse(self):
        node = self.__expr()
        if self.__token:
            raise SyntaxError("Invalid syntax")
        
        return node
    
if __name__ == "__main__":
    while((i := input()) != "end"):
        lexer = Lexer(i)
        parser = Parser(lexer)
        token = parser.parse().token
        print(token)


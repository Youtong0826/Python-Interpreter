from lexer import Lexer
from _ast_ import Node, DataNode, BinaryOperatorNode
from _token import DataType, Operator
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
        
    def __expr(self):
        node = self.__factor()
        while self.__token and isinstance(self.__token.type, Operator):
            op = self.__token
            self.__throw(op.type)
            node = BinaryOperatorNode(op, node, self.__factor())
            
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


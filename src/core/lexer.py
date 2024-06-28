from core._token import (
    DataType,
    Operator,
    Token
)

from typing import Union

class Lexer:
    def __init__(self, text: str = "") -> None:
        self.text = text
        self.__index = 0
        self.__size = len(text)
        self.__chr = text[0]
        
    def __advance(self):
        self.__index += 1
        self.__chr = self.text[self.__index] if self.__index < self.__size else None
        
    def __read_number(self):
        start = self.__index
        while self.__chr and self.__chr.isdecimal():
            self.__advance()
            
        return int(self.text[start:self.__index])      
    
    def next(self) -> Union[Token, None]:
        if (self.__index < self.__size):
            chr = self.__chr
            if chr.isdecimal():
                return Token(DataType.NUM, self.__read_number())
            
            self.__advance()
            return Token(Operator(chr), chr)
        

if __name__ == "__main__":
    test = "1+2*3/4-5"
    
    L = Lexer(test)
    while s := L.next():
        print(s)
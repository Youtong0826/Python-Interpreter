from core._token import (
    DataType,
    Operator,
    Prefix,
    Convert,
    Variable,
    Token
)

from typing import Union

class Lexer:
    def __init__(self, text: str) -> None:
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

    def __read_string(self):
        self.__advance()
        start = self.__index
        while self.__chr and self.__chr != '"':
            self.__advance()

        if self.__chr != '"':
            raise SyntaxError("unterminated string literal")

        end = self.__index
        self.__advance()
        return self.text[start:end]
    
    def __read_variable(self):
        start = self.__index
        while self.__chr and self.__chr != '=':
            self.__advance()

        val_name = self.text[start:self.__index]
        if self.__chr != '=':
            return Variable(val_name, None, Convert.missing())
        
        self.__advance()
        nxt = self.next()
        return Variable(val_name, nxt.value, nxt.type)
    
    def next(self) -> Union[Token, None]:
        if (self.__index < self.__size):
            chr = self.__chr
            
            match Convert.token_type(chr):
                case DataType.SPACE:
                    self.__advance()
                    return self.next()
                
                case DataType.VAR:
                    return Token(DataType.VAR, self.__read_variable())
                
                case DataType.STRING:
                    return Token(DataType.STRING, self.__read_string())

                case DataType.INT:
                    return Token(DataType.INT, self.__read_number())
                
                case DataType.CHR | _:
                    self.__advance()
                    return Token(Operator(chr), chr)
        

if __name__ == "__main__":
    test = "1+2*3/4-5"
    
    L = Lexer(test)
    while s := L.next():
        print(s)
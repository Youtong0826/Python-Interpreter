from dataclasses import dataclass
from typing import Union, Any
from enum import Enum

class Prefix(Enum):
    VAR = '?'
    FUNC = '$'

class Brackets(Enum):
    STRING = '"' # a string be like "abc"
    TUPLE = '('  # a tuple be like (1, 3.0, "abc")
    LIST = '['   # a list be like [0, 1, 2, 3]

class Operator(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    
class DataType(Enum):
    MISSING = 0
    INT = 1   # a integer number be like 123
    CHR = 2   # a character be like "c"
    FLOAT = 3 # a float number be like 3.14
    SPACE = 4
    STRING = 5
    VAR = 6

class Convert:
    @staticmethod
    def missing():
        return DataType.MISSING

    @staticmethod
    def integer():
        return DataType.INT
    
    @staticmethod
    def character():
        return DataType.CHR
    
    @staticmethod
    def float():
        return DataType.FLOAT
    
    @staticmethod
    def space():
        return DataType.SPACE
    
    @staticmethod
    def string():
        return DataType.STRING
    
    @staticmethod
    def token_type(val: str):
        if val.isdecimal():
            return Convert.integer()
        
        match val:
            case ' ':
                return Convert.space()
        
            case Brackets.STRING.value:
                return Convert.string()

            case Prefix.VAR.value:
                return DataType.VAR
            
            case _:
                return Convert.character()

@dataclass
class Variable:
    name: str
    value: Any
    type: Union[Operator, DataType]

    def __str__(self) -> str:
        return self.value
    
    def __repr__(self):
        return f"<Variable type={self.type} value={self.value}>"

@dataclass
class Token:
    type: Union[Operator, DataType]
    value: Any

    def __str__(self) -> str:
        return f"{self.type}: {self.value}"
    
    def __repr__(self):
        return f"<Token type={self.type} value={self.value}>"
    
if __name__ == "__main__":
    i = input()
    print(i.isdecimal())
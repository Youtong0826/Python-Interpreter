from dataclasses import dataclass
from enum import Enum
from typing import Union, Any

class Operator(Enum):
    ADD = '+'
    SUB = '-'
    MUL = '*'
    DIV = '/'
    
class DataType(Enum):
    NUM = 1
    CHR = 2

@dataclass
class Token:
    type: Union[Operator, DataType]
    value: Any
    
    def __str__(self) -> str:
        return f"{self.type}: {self.value}"
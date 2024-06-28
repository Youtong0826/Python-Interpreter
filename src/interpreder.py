from core import (
    NodeVisitor, 
    Parser, 
    Lexer)

class InterPreder(NodeVisitor):
    def __init__(self, text: str) -> None:
        super().__init__()
        self.__parser = Parser(Lexer(text))
        
    def calc(self):
        ast = self.__parser.parse()
        return self.visit(ast)
    
if __name__ == "__main__":
    while((i := input("[Arithmetic Interpreder]> ")) != "end"):
        ip = InterPreder(i)
        print("result:", ip.calc().value)
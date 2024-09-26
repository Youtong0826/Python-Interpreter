# 四則運算直譯器 (made with python)
分層介紹:
```
src/
├── core - [核心架構]
│   ├── _ast_.py [抽象語法樹]
│   ├── _token.py [符號]
│   ├── lexer.py [詞法分析器]
│   ├── parser.py [語法解析器]
│   ├── visitor.py [抽象語法樹的訪問器]
│   └── ...
│ 
└── interpreter.py [直譯器]
```
該直譯器的執行過程為: \
輸入 Input -> 詞法分析器 Lexer -> 符號 Token -> 語法分析器 Parser -> 抽象語法樹 AST -> 直譯器 Interpreter -> 結果 Result

## 詞法分析器 Lexer
辨識輸入的內容並轉換為一個個的符號 Token。

## 符號 Token
經過詞法分析器得到的結果，諸如變數，字串，關鍵字等等。

## 語法解析器 Parser
根據輸入的 Token 按照語法建立抽象語法樹 (Abstract Syntax Tree)。

## 抽象語法樹 Abstract Syntax Tree
代表著整個輸入程式碼的架構。

## 直譯器 Interpreter
按照語法解釋與遍歷抽象語法樹 (Abstract Syntax Tree) 並產生結果。

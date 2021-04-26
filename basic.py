import lexer
import parser_
import Interpreter_
# def printout(*args):
#     for itr in args:
#         if itr: print(itr)

while True:
    text = input("-> ")
    tokens, error = lexer.run("Shell",text)
    print(tokens)
    if error is not None:
        print(error.as_string())
    # Generate Absract Syntax Tree
    else:
        ast = parser_.create_ast(tokens)
        if ast.error:
            print(ast.node,ast.error.as_string())
        else:
            print(ast.node)
            interprrter = Interpreter_.run(ast.node)
            if interprrter.error:
                print(interprrter.error.as_string())
            else:
                print(interprrter.value)

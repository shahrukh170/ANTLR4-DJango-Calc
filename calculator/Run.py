from CalculatorXLexer import CalculatorXLexer
from CalculatorXParser import CalculatorXParser
##from CalculatorListener import CalculatorListener
##from PyListener import PyListener
from CalculatorXVisitor import CalculatorXVisitor
##from TableGenerator import TableGenerator
from CalculatorXBaseVisitorImpl import CalculatorXBaseVisitorImpl
import antlr4
from antlr4 import *

def beautify_lisp_string(in_string):
    indent_size = 3
    add_indent = ' '*indent_size
    out_string = in_string[0]  # no indent for 1st (
    indent = ''
    for i in range(1, len(in_string)):
        if in_string[i] == '(' and in_string[i+1] != ' ':
            indent += add_indent
            out_string += "\n" + indent + '('
        elif in_string[i] == ')':
            out_string += ')'
            if len(indent) > 0:
                indent = indent.replace(add_indent, '', 1)
        else:
            out_string += in_string[i]
    return out_string
#class CalculatorPrintListener(CalculatorListener):
#    def enterProgram(self, ctx):
#        print("Hello: %s" % ctx.ID())
def Run_Fun():
        file_name = './test2.mu'
        input_stream= FileStream(file_name)
        lexer = CalculatorXLexer(input_stream)
        print('input_stream:')
        print(input_stream)
        print()
        token_stream = CommonTokenStream(lexer)
        token_stream.fill()
        print('tokens:')
        for tk in token_stream.tokens:
            print(tk)
        print()
    
        parser = CalculatorXParser(token_stream)
        tree = parser.inputs()
        print('tree:')
        lisp_tree_str = tree.toStringTree(recog=parser)
        print(beautify_lisp_string(lisp_tree_str))
    
        
        lexer = CalculatorXLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = CalculatorXParser(stream)
        tree = parser.inputs()
        calcVisitor =CalculatorXBaseVisitorImpl()
        result = calcVisitor.visit(tree);
        print("Result: ",result)
    
        # test the parser with an input
        char_stream = FileStream(file_name)
        lexer = CalculatorXLexer(char_stream)
        tokens = CommonTokenStream(lexer)
        parser = CalculatorXParser(tokens)
    
        # print the parse tree
        t = parser.inputs()
        print(t.toStringTree())
        result = calcVisitor.visit(t);
        print("Result: ",result)



if __name__ == '__main__':
    a = Run_Fun()

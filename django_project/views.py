from django.shortcuts import render
#from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
#######################################################
# antlr 4 classes details 
######################################################
from calculator.CalculatorXLexer import CalculatorXLexer
from calculator.CalculatorXParser import CalculatorXParser
##from CalculatorListener import CalculatorListener
##from PyListener import PyListener
from calculator.CalculatorXVisitor import CalculatorXVisitor
##from TableGenerator import TableGenerator
from calculator.CalculatorXBaseVisitorImpl import CalculatorXBaseVisitorImpl
import antlr4
from antlr4 import *
########################################################
# Create your views here.
@csrf_exempt 
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
@csrf_exempt 
def Run_Fun(request):
    if request.method == "POST":
        usrname = request.POST['usrname']
        equation = request.POST['equation']
        file_name = 'django_project/test2.mu'
        if not equation == None:
             file_name = 'django_project/test3.mu' 
             fileX = open('django_project/test3.mu','w+')
             fileX.write(equation)
             fileX.close()
        else:
             file_name = 'django_project/test2.mu'
        # test the parser with an input
        char_stream = antlr4.FileStream(file_name)
        lexer = CalculatorXLexer(char_stream)
        tokens = antlr4.CommonTokenStream(lexer)
        parser = CalculatorXParser(tokens)
        calcVisitor =CalculatorXBaseVisitorImpl()
        # print the parse tree
        t = parser.inputs()
        #print(t.toStringTree())
        result = calcVisitor.visit(t);
        ##print("Result: ",result)
        context = {
          "usrname"  : usrname ,
          "inputstream" : char_stream,
          ####"lisptree"  :t.toStringTree(),
          ###beautify_lisp_string(lisp_tree_str),
          "result" : result 
        }
        return render(request, "result.html", context) 
###################################################  
# Create your views here.
@csrf_exempt 
def index(request):
    return render(request, "input.html")

@csrf_exempt 
def addition(request):
    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a + b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})


@csrf_exempt 
def substraction(request):
    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a - b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})

@csrf_exempt
def multiplication(request):

    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a * b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})


@csrf_exempt
def division(request):

    if request.method == "POST":
        num1 = request.POST['num1']
        num2 = request.POST['num2']

        if num1.isdigit() and num2.isdigit():
            a = int(num1)
            b = int(num2)
            res = a / b

            return render(request, "result.html", {"result": res})
        else:
            res = "Only digits are allowed"
            return render(request, "result.html", {"result": res})
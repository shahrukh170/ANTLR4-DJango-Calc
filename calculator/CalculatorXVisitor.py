# Generated from CalculatorX.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalculatorXParser import CalculatorXParser
else:
    from CalculatorXParser import CalculatorXParser

# This class defines a complete generic visitor for a parse tree produced by CalculatorXParser.

class CalculatorXVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalculatorXParser#ToSetVar.
    def visitToSetVar(self, ctx:CalculatorXParser.ToSetVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Calculate.
    def visitCalculate(self, ctx:CalculatorXParser.CalculateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#SetVariable.
    def visitSetVariable(self, ctx:CalculatorXParser.SetVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#ToMultOrDiv.
    def visitToMultOrDiv(self, ctx:CalculatorXParser.ToMultOrDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Plus.
    def visitPlus(self, ctx:CalculatorXParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Minus.
    def visitMinus(self, ctx:CalculatorXParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Multiplication.
    def visitMultiplication(self, ctx:CalculatorXParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Division.
    def visitDivision(self, ctx:CalculatorXParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#ToPow.
    def visitToPow(self, ctx:CalculatorXParser.ToPowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Power.
    def visitPower(self, ctx:CalculatorXParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#ChangeSign.
    def visitChangeSign(self, ctx:CalculatorXParser.ChangeSignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#ToAtom.
    def visitToAtom(self, ctx:CalculatorXParser.ToAtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#ConstantPI.
    def visitConstantPI(self, ctx:CalculatorXParser.ConstantPIContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#ConstantE.
    def visitConstantE(self, ctx:CalculatorXParser.ConstantEContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Double.
    def visitDouble(self, ctx:CalculatorXParser.DoubleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Int.
    def visitInt(self, ctx:CalculatorXParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Variable.
    def visitVariable(self, ctx:CalculatorXParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalculatorXParser#Braces.
    def visitBraces(self, ctx:CalculatorXParser.BracesContext):
        return self.visitChildren(ctx)



del CalculatorXParser
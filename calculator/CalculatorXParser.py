# Generated from CalculatorX.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("R\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\3\2\3\2\3\2\3\2\3\2\5\2\27\n\2\3\2\3\2\5\2\33")
        buf.write("\n\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\7\4*\n\4\f\4\16\4-\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\7\58\n\5\f\5\16\5;\13\5\3\6\3\6\3\6\5\6@\n\6")
        buf.write("\3\7\3\7\3\7\5\7E\n\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\b\5\bP\n\b\3\b\2\4\6\b\t\2\4\6\b\n\f\16\2\2\2W\2\32")
        buf.write("\3\2\2\2\4\34\3\2\2\2\6 \3\2\2\2\b.\3\2\2\2\n<\3\2\2\2")
        buf.write("\fD\3\2\2\2\16O\3\2\2\2\20\21\5\4\3\2\21\22\7\b\2\2\22")
        buf.write("\23\5\2\2\2\23\33\3\2\2\2\24\26\5\6\4\2\25\27\7\b\2\2")
        buf.write("\26\25\3\2\2\2\26\27\3\2\2\2\27\30\3\2\2\2\30\31\7\2\2")
        buf.write("\3\31\33\3\2\2\2\32\20\3\2\2\2\32\24\3\2\2\2\33\3\3\2")
        buf.write("\2\2\34\35\7\n\2\2\35\36\7\f\2\2\36\37\5\6\4\2\37\5\3")
        buf.write("\2\2\2 !\b\4\1\2!\"\5\b\5\2\"+\3\2\2\2#$\f\5\2\2$%\7\13")
        buf.write("\2\2%*\5\b\5\2&\'\f\4\2\2\'(\7\r\2\2(*\5\b\5\2)#\3\2\2")
        buf.write("\2)&\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3\2\2\2,\7\3\2\2\2")
        buf.write("-+\3\2\2\2./\b\5\1\2/\60\5\n\6\2\609\3\2\2\2\61\62\f\5")
        buf.write("\2\2\62\63\7\16\2\2\638\5\n\6\2\64\65\f\4\2\2\65\66\7")
        buf.write("\17\2\2\668\5\n\6\2\67\61\3\2\2\2\67\64\3\2\2\28;\3\2")
        buf.write("\2\29\67\3\2\2\29:\3\2\2\2:\t\3\2\2\2;9\3\2\2\2<?\5\f")
        buf.write("\7\2=>\7\7\2\2>@\5\n\6\2?=\3\2\2\2?@\3\2\2\2@\13\3\2\2")
        buf.write("\2AB\7\r\2\2BE\5\f\7\2CE\5\16\b\2DA\3\2\2\2DC\3\2\2\2")
        buf.write("E\r\3\2\2\2FP\7\5\2\2GP\7\6\2\2HP\7\4\2\2IP\7\3\2\2JP")
        buf.write("\7\n\2\2KL\7\20\2\2LM\5\6\4\2MN\7\21\2\2NP\3\2\2\2OF\3")
        buf.write("\2\2\2OG\3\2\2\2OH\3\2\2\2OI\3\2\2\2OJ\3\2\2\2OK\3\2\2")
        buf.write("\2P\17\3\2\2\2\13\26\32)+\679?DO")
        return buf.getvalue()


class CalculatorXParser ( Parser ):

    grammarFileName = "CalculatorX.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'pi'", "'e'", 
                     "'^'", "'\n'", "<INVALID>", "<INVALID>", "'+'", "'='", 
                     "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "INT", "DOUBLE", "PI", "E", "POW", "NL", 
                      "WS", "ID", "PLUS", "EQUAL", "MINUS", "MULT", "DIV", 
                      "LPAR", "RPAR" ]

    RULE_inputs = 0
    RULE_setVar = 1
    RULE_plusOrMinus = 2
    RULE_multOrDiv = 3
    RULE_pows = 4
    RULE_unaryMinus = 5
    RULE_atom = 6

    ruleNames =  [ "inputs", "setVar", "plusOrMinus", "multOrDiv", "pows", 
                   "unaryMinus", "atom" ]

    EOF = Token.EOF
    INT=1
    DOUBLE=2
    PI=3
    E=4
    POW=5
    NL=6
    WS=7
    ID=8
    PLUS=9
    EQUAL=10
    MINUS=11
    MULT=12
    DIV=13
    LPAR=14
    RPAR=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class InputsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorXParser.RULE_inputs

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class CalculateContext(InputsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.InputsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def plusOrMinus(self):
            return self.getTypedRuleContext(CalculatorXParser.PlusOrMinusContext,0)

        def EOF(self):
            return self.getToken(CalculatorXParser.EOF, 0)
        def NL(self):
            return self.getToken(CalculatorXParser.NL, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCalculate" ):
                return visitor.visitCalculate(self)
            else:
                return visitor.visitChildren(self)


    class ToSetVarContext(InputsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.InputsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def setVar(self):
            return self.getTypedRuleContext(CalculatorXParser.SetVarContext,0)

        def NL(self):
            return self.getToken(CalculatorXParser.NL, 0)
        def inputs(self):
            return self.getTypedRuleContext(CalculatorXParser.InputsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToSetVar" ):
                return visitor.visitToSetVar(self)
            else:
                return visitor.visitChildren(self)



    def inputs(self):

        localctx = CalculatorXParser.InputsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_inputs)
        self._la = 0 # Token type
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = CalculatorXParser.ToSetVarContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.setVar()
                self.state = 15
                self.match(CalculatorXParser.NL)
                self.state = 16
                self.inputs()
                pass

            elif la_ == 2:
                localctx = CalculatorXParser.CalculateContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 18
                self.plusOrMinus(0)
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==CalculatorXParser.NL:
                    self.state = 19
                    self.match(CalculatorXParser.NL)


                self.state = 22
                self.match(CalculatorXParser.EOF)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetVarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorXParser.RULE_setVar

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SetVariableContext(SetVarContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.SetVarContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculatorXParser.ID, 0)
        def EQUAL(self):
            return self.getToken(CalculatorXParser.EQUAL, 0)
        def plusOrMinus(self):
            return self.getTypedRuleContext(CalculatorXParser.PlusOrMinusContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetVariable" ):
                return visitor.visitSetVariable(self)
            else:
                return visitor.visitChildren(self)



    def setVar(self):

        localctx = CalculatorXParser.SetVarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_setVar)
        try:
            localctx = CalculatorXParser.SetVariableContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(CalculatorXParser.ID)
            self.state = 27
            self.match(CalculatorXParser.EQUAL)
            self.state = 28
            self.plusOrMinus(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PlusOrMinusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorXParser.RULE_plusOrMinus

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ToMultOrDivContext(PlusOrMinusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.PlusOrMinusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multOrDiv(self):
            return self.getTypedRuleContext(CalculatorXParser.MultOrDivContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToMultOrDiv" ):
                return visitor.visitToMultOrDiv(self)
            else:
                return visitor.visitChildren(self)


    class PlusContext(PlusOrMinusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.PlusOrMinusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def plusOrMinus(self):
            return self.getTypedRuleContext(CalculatorXParser.PlusOrMinusContext,0)

        def PLUS(self):
            return self.getToken(CalculatorXParser.PLUS, 0)
        def multOrDiv(self):
            return self.getTypedRuleContext(CalculatorXParser.MultOrDivContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPlus" ):
                return visitor.visitPlus(self)
            else:
                return visitor.visitChildren(self)


    class MinusContext(PlusOrMinusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.PlusOrMinusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def plusOrMinus(self):
            return self.getTypedRuleContext(CalculatorXParser.PlusOrMinusContext,0)

        def MINUS(self):
            return self.getToken(CalculatorXParser.MINUS, 0)
        def multOrDiv(self):
            return self.getTypedRuleContext(CalculatorXParser.MultOrDivContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMinus" ):
                return visitor.visitMinus(self)
            else:
                return visitor.visitChildren(self)



    def plusOrMinus(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorXParser.PlusOrMinusContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_plusOrMinus, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalculatorXParser.ToMultOrDivContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 31
            self.multOrDiv(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 41
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 39
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorXParser.PlusContext(self, CalculatorXParser.PlusOrMinusContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_plusOrMinus)
                        self.state = 33
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 34
                        self.match(CalculatorXParser.PLUS)
                        self.state = 35
                        self.multOrDiv(0)
                        pass

                    elif la_ == 2:
                        localctx = CalculatorXParser.MinusContext(self, CalculatorXParser.PlusOrMinusContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_plusOrMinus)
                        self.state = 36
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 37
                        self.match(CalculatorXParser.MINUS)
                        self.state = 38
                        self.multOrDiv(0)
                        pass

             
                self.state = 43
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultOrDivContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorXParser.RULE_multOrDiv

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicationContext(MultOrDivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.MultOrDivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multOrDiv(self):
            return self.getTypedRuleContext(CalculatorXParser.MultOrDivContext,0)

        def MULT(self):
            return self.getToken(CalculatorXParser.MULT, 0)
        def pows(self):
            return self.getTypedRuleContext(CalculatorXParser.PowsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplication" ):
                return visitor.visitMultiplication(self)
            else:
                return visitor.visitChildren(self)


    class DivisionContext(MultOrDivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.MultOrDivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def multOrDiv(self):
            return self.getTypedRuleContext(CalculatorXParser.MultOrDivContext,0)

        def DIV(self):
            return self.getToken(CalculatorXParser.DIV, 0)
        def pows(self):
            return self.getTypedRuleContext(CalculatorXParser.PowsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDivision" ):
                return visitor.visitDivision(self)
            else:
                return visitor.visitChildren(self)


    class ToPowContext(MultOrDivContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.MultOrDivContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def pows(self):
            return self.getTypedRuleContext(CalculatorXParser.PowsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToPow" ):
                return visitor.visitToPow(self)
            else:
                return visitor.visitChildren(self)



    def multOrDiv(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculatorXParser.MultOrDivContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_multOrDiv, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = CalculatorXParser.ToPowContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 45
            self.pows()
            self._ctx.stop = self._input.LT(-1)
            self.state = 55
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 53
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = CalculatorXParser.MultiplicationContext(self, CalculatorXParser.MultOrDivContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multOrDiv)
                        self.state = 47
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 48
                        self.match(CalculatorXParser.MULT)
                        self.state = 49
                        self.pows()
                        pass

                    elif la_ == 2:
                        localctx = CalculatorXParser.DivisionContext(self, CalculatorXParser.MultOrDivContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multOrDiv)
                        self.state = 50
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 51
                        self.match(CalculatorXParser.DIV)
                        self.state = 52
                        self.pows()
                        pass

             
                self.state = 57
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class PowsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorXParser.RULE_pows

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class PowerContext(PowsContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.PowsContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryMinus(self):
            return self.getTypedRuleContext(CalculatorXParser.UnaryMinusContext,0)

        def POW(self):
            return self.getToken(CalculatorXParser.POW, 0)
        def pows(self):
            return self.getTypedRuleContext(CalculatorXParser.PowsContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPower" ):
                return visitor.visitPower(self)
            else:
                return visitor.visitChildren(self)



    def pows(self):

        localctx = CalculatorXParser.PowsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_pows)
        try:
            localctx = CalculatorXParser.PowerContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.unaryMinus()
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 59
                self.match(CalculatorXParser.POW)
                self.state = 60
                self.pows()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryMinusContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorXParser.RULE_unaryMinus

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ChangeSignContext(UnaryMinusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.UnaryMinusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def MINUS(self):
            return self.getToken(CalculatorXParser.MINUS, 0)
        def unaryMinus(self):
            return self.getTypedRuleContext(CalculatorXParser.UnaryMinusContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChangeSign" ):
                return visitor.visitChangeSign(self)
            else:
                return visitor.visitChildren(self)


    class ToAtomContext(UnaryMinusContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.UnaryMinusContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(CalculatorXParser.AtomContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitToAtom" ):
                return visitor.visitToAtom(self)
            else:
                return visitor.visitChildren(self)



    def unaryMinus(self):

        localctx = CalculatorXParser.UnaryMinusContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryMinus)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculatorXParser.MINUS]:
                localctx = CalculatorXParser.ChangeSignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(CalculatorXParser.MINUS)
                self.state = 64
                self.unaryMinus()
                pass
            elif token in [CalculatorXParser.INT, CalculatorXParser.DOUBLE, CalculatorXParser.PI, CalculatorXParser.E, CalculatorXParser.ID, CalculatorXParser.LPAR]:
                localctx = CalculatorXParser.ToAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.atom()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculatorXParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ConstantPIContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PI(self):
            return self.getToken(CalculatorXParser.PI, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantPI" ):
                return visitor.visitConstantPI(self)
            else:
                return visitor.visitChildren(self)


    class VariableContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(CalculatorXParser.ID, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class BracesContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(CalculatorXParser.LPAR, 0)
        def plusOrMinus(self):
            return self.getTypedRuleContext(CalculatorXParser.PlusOrMinusContext,0)

        def RPAR(self):
            return self.getToken(CalculatorXParser.RPAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBraces" ):
                return visitor.visitBraces(self)
            else:
                return visitor.visitChildren(self)


    class ConstantEContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def E(self):
            return self.getToken(CalculatorXParser.E, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantE" ):
                return visitor.visitConstantE(self)
            else:
                return visitor.visitChildren(self)


    class DoubleContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def DOUBLE(self):
            return self.getToken(CalculatorXParser.DOUBLE, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDouble" ):
                return visitor.visitDouble(self)
            else:
                return visitor.visitChildren(self)


    class IntContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculatorXParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(CalculatorXParser.INT, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInt" ):
                return visitor.visitInt(self)
            else:
                return visitor.visitChildren(self)



    def atom(self):

        localctx = CalculatorXParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [CalculatorXParser.PI]:
                localctx = CalculatorXParser.ConstantPIContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(CalculatorXParser.PI)
                pass
            elif token in [CalculatorXParser.E]:
                localctx = CalculatorXParser.ConstantEContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(CalculatorXParser.E)
                pass
            elif token in [CalculatorXParser.DOUBLE]:
                localctx = CalculatorXParser.DoubleContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(CalculatorXParser.DOUBLE)
                pass
            elif token in [CalculatorXParser.INT]:
                localctx = CalculatorXParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.match(CalculatorXParser.INT)
                pass
            elif token in [CalculatorXParser.ID]:
                localctx = CalculatorXParser.VariableContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.match(CalculatorXParser.ID)
                pass
            elif token in [CalculatorXParser.LPAR]:
                localctx = CalculatorXParser.BracesContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.match(CalculatorXParser.LPAR)
                self.state = 74
                self.plusOrMinus(0)
                self.state = 75
                self.match(CalculatorXParser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.plusOrMinus_sempred
        self._predicates[3] = self.multOrDiv_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def plusOrMinus_sempred(self, localctx:PlusOrMinusContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multOrDiv_sempred(self, localctx:MultOrDivContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         





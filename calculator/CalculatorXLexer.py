# Generated from CalculatorX.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\6\2#\n\2\r\2\16\2$\3\3\6")
        buf.write("\3(\n\3\r\3\16\3)\3\3\3\3\6\3.\n\3\r\3\16\3/\3\4\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\6\b<\n\b\r\b\16\b=\3\b")
        buf.write("\3\b\3\t\3\t\7\tD\n\t\f\t\16\tG\13\t\3\n\3\n\3\13\3\13")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\2\2\21")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21\3\2\6\3\2\62;\5\2\13\13\17\17\"")
        buf.write("\"\5\2C\\aac|\6\2\62;C\\aac|\2Z\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\3\"\3\2\2\2\5\'\3\2\2\2\7\61\3\2\2\2\t\64\3\2\2")
        buf.write("\2\13\66\3\2\2\2\r8\3\2\2\2\17;\3\2\2\2\21A\3\2\2\2\23")
        buf.write("H\3\2\2\2\25J\3\2\2\2\27L\3\2\2\2\31N\3\2\2\2\33P\3\2")
        buf.write("\2\2\35R\3\2\2\2\37T\3\2\2\2!#\t\2\2\2\"!\3\2\2\2#$\3")
        buf.write("\2\2\2$\"\3\2\2\2$%\3\2\2\2%\4\3\2\2\2&(\t\2\2\2\'&\3")
        buf.write("\2\2\2()\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*+\3\2\2\2+-\7\60")
        buf.write("\2\2,.\t\2\2\2-,\3\2\2\2./\3\2\2\2/-\3\2\2\2/\60\3\2\2")
        buf.write("\2\60\6\3\2\2\2\61\62\7r\2\2\62\63\7k\2\2\63\b\3\2\2\2")
        buf.write("\64\65\7g\2\2\65\n\3\2\2\2\66\67\7`\2\2\67\f\3\2\2\28")
        buf.write("9\7\f\2\29\16\3\2\2\2:<\t\3\2\2;:\3\2\2\2<=\3\2\2\2=;")
        buf.write("\3\2\2\2=>\3\2\2\2>?\3\2\2\2?@\b\b\2\2@\20\3\2\2\2AE\t")
        buf.write("\4\2\2BD\t\5\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2EF\3\2\2")
        buf.write("\2F\22\3\2\2\2GE\3\2\2\2HI\7-\2\2I\24\3\2\2\2JK\7?\2\2")
        buf.write("K\26\3\2\2\2LM\7/\2\2M\30\3\2\2\2NO\7,\2\2O\32\3\2\2\2")
        buf.write("PQ\7\61\2\2Q\34\3\2\2\2RS\7*\2\2S\36\3\2\2\2TU\7+\2\2")
        buf.write("U \3\2\2\2\b\2$)/=E\3\b\2\2")
        return buf.getvalue()


class CalculatorXLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INT = 1
    DOUBLE = 2
    PI = 3
    E = 4
    POW = 5
    NL = 6
    WS = 7
    ID = 8
    PLUS = 9
    EQUAL = 10
    MINUS = 11
    MULT = 12
    DIV = 13
    LPAR = 14
    RPAR = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'pi'", "'e'", "'^'", "'\n'", "'+'", "'='", "'-'", "'*'", "'/'", 
            "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "DOUBLE", "PI", "E", "POW", "NL", "WS", "ID", "PLUS", 
            "EQUAL", "MINUS", "MULT", "DIV", "LPAR", "RPAR" ]

    ruleNames = [ "INT", "DOUBLE", "PI", "E", "POW", "NL", "WS", "ID", "PLUS", 
                  "EQUAL", "MINUS", "MULT", "DIV", "LPAR", "RPAR" ]

    grammarFileName = "CalculatorX.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



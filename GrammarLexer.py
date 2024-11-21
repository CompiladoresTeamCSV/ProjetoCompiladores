# Generated from Grammar.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,6,38,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,
        0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,2,4,2,27,8,2,11,
        2,12,2,28,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,0,0,6,1,1,3,2,5,3,7,4,
        9,5,11,6,1,0,2,2,0,65,90,97,122,2,0,10,10,32,32,38,0,1,1,0,0,0,0,
        3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,1,13,
        1,0,0,0,3,21,1,0,0,0,5,26,1,0,0,0,7,30,1,0,0,0,9,32,1,0,0,0,11,34,
        1,0,0,0,13,14,5,100,0,0,14,15,5,101,0,0,15,16,5,99,0,0,16,17,5,108,
        0,0,17,18,5,97,0,0,18,19,5,114,0,0,19,20,5,101,0,0,20,2,1,0,0,0,
        21,22,5,117,0,0,22,23,5,115,0,0,23,24,5,101,0,0,24,4,1,0,0,0,25,
        27,7,0,0,0,26,25,1,0,0,0,27,28,1,0,0,0,28,26,1,0,0,0,28,29,1,0,0,
        0,29,6,1,0,0,0,30,31,5,123,0,0,31,8,1,0,0,0,32,33,5,125,0,0,33,10,
        1,0,0,0,34,35,7,1,0,0,35,36,1,0,0,0,36,37,6,5,0,0,37,12,1,0,0,0,
        2,0,28,1,6,0,0
    ]

class GrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    DECLARE = 1
    USE = 2
    VAR = 3
    ACHAVE = 4
    FCHAVE = 5
    BRANCO = 6

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'declare'", "'use'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "DECLARE", "USE", "VAR", "ACHAVE", "FCHAVE", "BRANCO" ]

    ruleNames = [ "DECLARE", "USE", "VAR", "ACHAVE", "FCHAVE", "BRANCO" ]

    grammarFileName = "Grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



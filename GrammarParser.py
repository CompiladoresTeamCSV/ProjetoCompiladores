# Generated from Grammar.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,6,23,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,5,1,13,
        8,1,10,1,12,1,16,9,1,1,1,1,1,1,1,3,1,21,8,1,1,1,0,0,2,0,2,0,0,23,
        0,4,1,0,0,0,2,20,1,0,0,0,4,5,3,2,1,0,5,6,5,0,0,1,6,1,1,0,0,0,7,8,
        5,1,0,0,8,9,5,3,0,0,9,21,3,2,1,0,10,14,5,4,0,0,11,13,3,2,1,0,12,
        11,1,0,0,0,13,16,1,0,0,0,14,12,1,0,0,0,14,15,1,0,0,0,15,17,1,0,0,
        0,16,14,1,0,0,0,17,21,5,5,0,0,18,19,5,2,0,0,19,21,5,3,0,0,20,7,1,
        0,0,0,20,10,1,0,0,0,20,18,1,0,0,0,21,3,1,0,0,0,2,14,20
    ]

class GrammarParser ( Parser ):

    grammarFileName = "Grammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'declare'", "'use'", "<INVALID>", "'{'", 
                     "'}'" ]

    symbolicNames = [ "<INVALID>", "DECLARE", "USE", "VAR", "ACHAVE", "FCHAVE", 
                      "BRANCO" ]

    RULE_prog = 0
    RULE_com = 1

    ruleNames =  [ "prog", "com" ]

    EOF = Token.EOF
    DECLARE=1
    USE=2
    VAR=3
    ACHAVE=4
    FCHAVE=5
    BRANCO=6

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def com(self):
            return self.getTypedRuleContext(GrammarParser.ComContext,0)


        def EOF(self):
            return self.getToken(GrammarParser.EOF, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = GrammarParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.com()
            self.state = 5
            self.match(GrammarParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(GrammarParser.DECLARE, 0)

        def VAR(self):
            return self.getToken(GrammarParser.VAR, 0)

        def com(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarParser.ComContext)
            else:
                return self.getTypedRuleContext(GrammarParser.ComContext,i)


        def ACHAVE(self):
            return self.getToken(GrammarParser.ACHAVE, 0)

        def FCHAVE(self):
            return self.getToken(GrammarParser.FCHAVE, 0)

        def USE(self):
            return self.getToken(GrammarParser.USE, 0)

        def getRuleIndex(self):
            return GrammarParser.RULE_com

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCom" ):
                listener.enterCom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCom" ):
                listener.exitCom(self)




    def com(self):

        localctx = GrammarParser.ComContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_com)
        self._la = 0 # Token type
        try:
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 7
                self.match(GrammarParser.DECLARE)
                self.state = 8
                self.match(GrammarParser.VAR)
                self.state = 9
                self.com()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 10
                self.match(GrammarParser.ACHAVE)
                self.state = 14
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 22) != 0):
                    self.state = 11
                    self.com()
                    self.state = 16
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 17
                self.match(GrammarParser.FCHAVE)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 18
                self.match(GrammarParser.USE)
                self.state = 19
                self.match(GrammarParser.VAR)
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






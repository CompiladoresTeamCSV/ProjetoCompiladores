# Generated from Gramatica_dados.g4 by ANTLR 4.13.2
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
        4,1,18,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,3,1,22,8,1,1,1,3,1,25,8,1,
        1,1,1,1,1,2,1,2,1,3,1,3,4,3,33,8,3,11,3,12,3,34,3,3,37,8,3,1,4,1,
        4,1,4,1,4,1,4,3,4,44,8,4,1,5,1,5,1,5,0,0,6,0,2,4,6,8,10,0,3,1,0,
        13,14,2,0,12,12,15,15,1,0,1,10,47,0,13,1,0,0,0,2,19,1,0,0,0,4,28,
        1,0,0,0,6,36,1,0,0,0,8,38,1,0,0,0,10,45,1,0,0,0,12,14,3,2,1,0,13,
        12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,1,0,0,
        0,17,18,5,0,0,1,18,1,1,0,0,0,19,21,3,4,2,0,20,22,3,6,3,0,21,20,1,
        0,0,0,21,22,1,0,0,0,22,24,1,0,0,0,23,25,3,8,4,0,24,23,1,0,0,0,24,
        25,1,0,0,0,25,26,1,0,0,0,26,27,5,11,0,0,27,3,1,0,0,0,28,29,3,10,
        5,0,29,5,1,0,0,0,30,37,7,0,0,0,31,33,7,1,0,0,32,31,1,0,0,0,33,34,
        1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,37,1,0,0,0,36,30,1,0,0,0,
        36,32,1,0,0,0,37,7,1,0,0,0,38,39,5,14,0,0,39,40,5,16,0,0,40,43,7,
        1,0,0,41,42,5,17,0,0,42,44,3,8,4,0,43,41,1,0,0,0,43,44,1,0,0,0,44,
        9,1,0,0,0,45,46,7,2,0,0,46,11,1,0,0,0,6,15,21,24,34,36,43
    ]

class Gramatica_dadosParser ( Parser ):

    grammarFileName = "Gramatica_dados.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'filtre'", "'carregue'", "'salve'", "'some'", 
                     "'media'", "'conte'", "'min'", "'max'", "'ordene'", 
                     "'exporte'", "';'" ]

    symbolicNames = [ "<INVALID>", "FILTER", "LOAD", "SAVE", "SUM", "AVG", 
                      "COUNT", "MIN", "MAX", "SORT", "EXPORT", "END_OF_LINE", 
                      "STRING", "FILE", "ID", "NUMBER", "OPERATOR", "LOGICAL_OPERATOR", 
                      "BRANCO" ]

    RULE_prog = 0
    RULE_pedido = 1
    RULE_comando = 2
    RULE_parametros = 3
    RULE_condicao = 4
    RULE_action = 5

    ruleNames =  [ "prog", "pedido", "comando", "parametros", "condicao", 
                   "action" ]

    EOF = Token.EOF
    FILTER=1
    LOAD=2
    SAVE=3
    SUM=4
    AVG=5
    COUNT=6
    MIN=7
    MAX=8
    SORT=9
    EXPORT=10
    END_OF_LINE=11
    STRING=12
    FILE=13
    ID=14
    NUMBER=15
    OPERATOR=16
    LOGICAL_OPERATOR=17
    BRANCO=18

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

        def EOF(self):
            return self.getToken(Gramatica_dadosParser.EOF, 0)

        def pedido(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Gramatica_dadosParser.PedidoContext)
            else:
                return self.getTypedRuleContext(Gramatica_dadosParser.PedidoContext,i)


        def getRuleIndex(self):
            return Gramatica_dadosParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = Gramatica_dadosParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.pedido()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2046) != 0)):
                    break

            self.state = 17
            self.match(Gramatica_dadosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PedidoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comando(self):
            return self.getTypedRuleContext(Gramatica_dadosParser.ComandoContext,0)


        def END_OF_LINE(self):
            return self.getToken(Gramatica_dadosParser.END_OF_LINE, 0)

        def parametros(self):
            return self.getTypedRuleContext(Gramatica_dadosParser.ParametrosContext,0)


        def condicao(self):
            return self.getTypedRuleContext(Gramatica_dadosParser.CondicaoContext,0)


        def getRuleIndex(self):
            return Gramatica_dadosParser.RULE_pedido

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPedido" ):
                listener.enterPedido(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPedido" ):
                listener.exitPedido(self)




    def pedido(self):

        localctx = Gramatica_dadosParser.PedidoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pedido)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.comando()
            self.state = 21
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 20
                self.parametros()


            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 23
                self.condicao()


            self.state = 26
            self.match(Gramatica_dadosParser.END_OF_LINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComandoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def action(self):
            return self.getTypedRuleContext(Gramatica_dadosParser.ActionContext,0)


        def getRuleIndex(self):
            return Gramatica_dadosParser.RULE_comando

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComando" ):
                listener.enterComando(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComando" ):
                listener.exitComando(self)




    def comando(self):

        localctx = Gramatica_dadosParser.ComandoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_comando)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.action()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Gramatica_dadosParser.ID, 0)

        def FILE(self):
            return self.getToken(Gramatica_dadosParser.FILE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(Gramatica_dadosParser.STRING)
            else:
                return self.getToken(Gramatica_dadosParser.STRING, i)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(Gramatica_dadosParser.NUMBER)
            else:
                return self.getToken(Gramatica_dadosParser.NUMBER, i)

        def getRuleIndex(self):
            return Gramatica_dadosParser.RULE_parametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametros" ):
                listener.enterParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametros" ):
                listener.exitParametros(self)




    def parametros(self):

        localctx = Gramatica_dadosParser.ParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parametros)
        self._la = 0 # Token type
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                _la = self._input.LA(1)
                if not(_la==13 or _la==14):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass
            elif token in [12, 15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 32 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 31
                    _la = self._input.LA(1)
                    if not(_la==12 or _la==15):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 34 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==12 or _la==15):
                        break

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


    class CondicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(Gramatica_dadosParser.ID, 0)

        def OPERATOR(self):
            return self.getToken(Gramatica_dadosParser.OPERATOR, 0)

        def STRING(self):
            return self.getToken(Gramatica_dadosParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(Gramatica_dadosParser.NUMBER, 0)

        def LOGICAL_OPERATOR(self):
            return self.getToken(Gramatica_dadosParser.LOGICAL_OPERATOR, 0)

        def condicao(self):
            return self.getTypedRuleContext(Gramatica_dadosParser.CondicaoContext,0)


        def getRuleIndex(self):
            return Gramatica_dadosParser.RULE_condicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicao" ):
                listener.enterCondicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicao" ):
                listener.exitCondicao(self)




    def condicao(self):

        localctx = Gramatica_dadosParser.CondicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_condicao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(Gramatica_dadosParser.ID)
            self.state = 39
            self.match(Gramatica_dadosParser.OPERATOR)
            self.state = 40
            _la = self._input.LA(1)
            if not(_la==12 or _la==15):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 41
                self.match(Gramatica_dadosParser.LOGICAL_OPERATOR)
                self.state = 42
                self.condicao()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FILTER(self):
            return self.getToken(Gramatica_dadosParser.FILTER, 0)

        def LOAD(self):
            return self.getToken(Gramatica_dadosParser.LOAD, 0)

        def SAVE(self):
            return self.getToken(Gramatica_dadosParser.SAVE, 0)

        def SUM(self):
            return self.getToken(Gramatica_dadosParser.SUM, 0)

        def AVG(self):
            return self.getToken(Gramatica_dadosParser.AVG, 0)

        def COUNT(self):
            return self.getToken(Gramatica_dadosParser.COUNT, 0)

        def MIN(self):
            return self.getToken(Gramatica_dadosParser.MIN, 0)

        def MAX(self):
            return self.getToken(Gramatica_dadosParser.MAX, 0)

        def SORT(self):
            return self.getToken(Gramatica_dadosParser.SORT, 0)

        def EXPORT(self):
            return self.getToken(Gramatica_dadosParser.EXPORT, 0)

        def getRuleIndex(self):
            return Gramatica_dadosParser.RULE_action

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAction" ):
                listener.enterAction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAction" ):
                listener.exitAction(self)




    def action(self):

        localctx = Gramatica_dadosParser.ActionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_action)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2046) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






# Generated from CalculadoraPractica.g4 by ANTLR 4.13.2
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
        4,1,11,40,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,3,1,19,8,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        5,1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,2,1,2,1,2,0,1,2,3,0,2,
        4,0,3,1,0,3,4,2,0,1,1,5,5,1,0,8,9,42,0,6,1,0,0,0,2,18,1,0,0,0,4,
        34,1,0,0,0,6,7,3,2,1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,6,1,-1,0,10,
        11,5,1,0,0,11,19,3,2,1,7,12,19,3,4,2,0,13,14,5,6,0,0,14,15,3,2,1,
        0,15,16,5,7,0,0,16,19,1,0,0,0,17,19,5,10,0,0,18,9,1,0,0,0,18,12,
        1,0,0,0,18,13,1,0,0,0,18,17,1,0,0,0,19,31,1,0,0,0,20,21,10,6,0,0,
        21,22,5,2,0,0,22,30,3,2,1,7,23,24,10,5,0,0,24,25,7,0,0,0,25,30,3,
        2,1,6,26,27,10,4,0,0,27,28,7,1,0,0,28,30,3,2,1,5,29,20,1,0,0,0,29,
        23,1,0,0,0,29,26,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,
        0,32,3,1,0,0,0,33,31,1,0,0,0,34,35,7,2,0,0,35,36,5,6,0,0,36,37,3,
        2,1,0,37,38,5,7,0,0,38,5,1,0,0,0,3,18,29,31
    ]

class CalculadoraPracticaParser ( Parser ):

    grammarFileName = "CalculadoraPractica.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'", "'^'", "'*'", "'/'", "'+'", "'('", 
                     "')'", "'sqrt'", "'abs'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "WS" ]

    RULE_prog = 0
    RULE_expresion = 1
    RULE_func = 2

    ruleNames =  [ "prog", "expresion", "func" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUMBER=10
    WS=11

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

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraPracticaParser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(CalculadoraPracticaParser.EOF, 0)

        def getRuleIndex(self):
            return CalculadoraPracticaParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = CalculadoraPracticaParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.expresion(0)
            self.state = 7
            self.match(CalculadoraPracticaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CalculadoraPracticaParser.RULE_expresion

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumeroContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraPracticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NUMBER(self):
            return self.getToken(CalculadoraPracticaParser.NUMBER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumero" ):
                listener.enterNumero(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumero" ):
                listener.exitNumero(self)


    class FuncionContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraPracticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def func(self):
            return self.getTypedRuleContext(CalculadoraPracticaParser.FuncContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncion" ):
                listener.enterFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncion" ):
                listener.exitFuncion(self)


    class AddSubContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraPracticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraPracticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraPracticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class ParentesisContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraPracticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraPracticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParentesis" ):
                listener.enterParentesis(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParentesis" ):
                listener.exitParentesis(self)


    class PotenciaContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraPracticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraPracticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraPracticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPotencia" ):
                listener.enterPotencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPotencia" ):
                listener.exitPotencia(self)


    class NegativoContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraPracticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraPracticaParser.ExpresionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativo" ):
                listener.enterNegativo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativo" ):
                listener.exitNegativo(self)


    class MultDivContext(ExpresionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a CalculadoraPracticaParser.ExpresionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CalculadoraPracticaParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(CalculadoraPracticaParser.ExpresionContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultDiv" ):
                listener.enterMultDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultDiv" ):
                listener.exitMultDiv(self)



    def expresion(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CalculadoraPracticaParser.ExpresionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_expresion, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                localctx = CalculadoraPracticaParser.NegativoContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 10
                self.match(CalculadoraPracticaParser.T__0)
                self.state = 11
                self.expresion(7)
                pass
            elif token in [8, 9]:
                localctx = CalculadoraPracticaParser.FuncionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.func()
                pass
            elif token in [6]:
                localctx = CalculadoraPracticaParser.ParentesisContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 13
                self.match(CalculadoraPracticaParser.T__5)
                self.state = 14
                self.expresion(0)
                self.state = 15
                self.match(CalculadoraPracticaParser.T__6)
                pass
            elif token in [10]:
                localctx = CalculadoraPracticaParser.NumeroContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 17
                self.match(CalculadoraPracticaParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 31
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 29
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        localctx = CalculadoraPracticaParser.PotenciaContext(self, CalculadoraPracticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 20
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 21
                        self.match(CalculadoraPracticaParser.T__1)
                        self.state = 22
                        self.expresion(7)
                        pass

                    elif la_ == 2:
                        localctx = CalculadoraPracticaParser.MultDivContext(self, CalculadoraPracticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 23
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 24
                        _la = self._input.LA(1)
                        if not(_la==3 or _la==4):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 25
                        self.expresion(6)
                        pass

                    elif la_ == 3:
                        localctx = CalculadoraPracticaParser.AddSubContext(self, CalculadoraPracticaParser.ExpresionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expresion)
                        self.state = 26
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 27
                        _la = self._input.LA(1)
                        if not(_la==1 or _la==5):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 28
                        self.expresion(5)
                        pass

             
                self.state = 33
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class FuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(CalculadoraPracticaParser.ExpresionContext,0)


        def getRuleIndex(self):
            return CalculadoraPracticaParser.RULE_func

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunc" ):
                listener.enterFunc(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunc" ):
                listener.exitFunc(self)




    def func(self):

        localctx = CalculadoraPracticaParser.FuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_func)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 35
            self.match(CalculadoraPracticaParser.T__5)
            self.state = 36
            self.expresion(0)
            self.state = 37
            self.match(CalculadoraPracticaParser.T__6)
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
        self._predicates[1] = self.expresion_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expresion_sempred(self, localctx:ExpresionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         





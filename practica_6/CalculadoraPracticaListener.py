# Generated from CalculadoraPractica.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CalculadoraPracticaParser import CalculadoraPracticaParser
else:
    from CalculadoraPracticaParser import CalculadoraPracticaParser

# This class defines a complete listener for a parse tree produced by CalculadoraPracticaParser.
class CalculadoraPracticaListener(ParseTreeListener):

    # Enter a parse tree produced by CalculadoraPracticaParser#prog.
    def enterProg(self, ctx:CalculadoraPracticaParser.ProgContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#prog.
    def exitProg(self, ctx:CalculadoraPracticaParser.ProgContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#Numero.
    def enterNumero(self, ctx:CalculadoraPracticaParser.NumeroContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#Numero.
    def exitNumero(self, ctx:CalculadoraPracticaParser.NumeroContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#Funcion.
    def enterFuncion(self, ctx:CalculadoraPracticaParser.FuncionContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#Funcion.
    def exitFuncion(self, ctx:CalculadoraPracticaParser.FuncionContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#AddSub.
    def enterAddSub(self, ctx:CalculadoraPracticaParser.AddSubContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#AddSub.
    def exitAddSub(self, ctx:CalculadoraPracticaParser.AddSubContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#Parentesis.
    def enterParentesis(self, ctx:CalculadoraPracticaParser.ParentesisContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#Parentesis.
    def exitParentesis(self, ctx:CalculadoraPracticaParser.ParentesisContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#Potencia.
    def enterPotencia(self, ctx:CalculadoraPracticaParser.PotenciaContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#Potencia.
    def exitPotencia(self, ctx:CalculadoraPracticaParser.PotenciaContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#Negativo.
    def enterNegativo(self, ctx:CalculadoraPracticaParser.NegativoContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#Negativo.
    def exitNegativo(self, ctx:CalculadoraPracticaParser.NegativoContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#MultDiv.
    def enterMultDiv(self, ctx:CalculadoraPracticaParser.MultDivContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#MultDiv.
    def exitMultDiv(self, ctx:CalculadoraPracticaParser.MultDivContext):
        pass


    # Enter a parse tree produced by CalculadoraPracticaParser#func.
    def enterFunc(self, ctx:CalculadoraPracticaParser.FuncContext):
        pass

    # Exit a parse tree produced by CalculadoraPracticaParser#func.
    def exitFunc(self, ctx:CalculadoraPracticaParser.FuncContext):
        pass



del CalculadoraPracticaParser
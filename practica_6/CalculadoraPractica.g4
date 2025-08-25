//antlr4 -Dlanguage=Python3 CalculadoraPractica.g4
//antlr4-parse CalculadoraPractica.g4 prog -tokens < test.txt

grammar CalculadoraPractica;

prog: expresion EOF ;

// Reglas principales con precedencia
expresion
    : '-' expresion                       # Negativo         
    | expresion '^' expresion             # Potencia         
    | expresion ('*' | '/') expresion     # MultDiv
    | expresion ('+' | '-') expresion     # AddSub
    | func                                # Funcion
    | '(' expresion ')'                   # Parentesis
    | NUMBER                              # Numero
    ;

// Funciones básicas: sqrt, abs, etc.
func
    : ('sqrt' | 'abs') '(' expresion ')'
    ;

// Tokens
NUMBER : [0-9]+ ('.' [0-9]+)? ;
WS     : [ \t\r\n]+ -> skip ;

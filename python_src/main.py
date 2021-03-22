'''
Solutions to exercises from https://ruslanspivak.com/lsbasi-part10/

Programming Exercises
1. If you haven’t done so yet, then, as an exercise, re-implement the interpreter in this article without looking at the source code and use part10.pas as your test input file
(This time I did a compiler to Python)
'''

import sys;sys.setrecursionlimit(50)

from lexer import Lexer
from astparser import Parser

from semantic_analyser import *
from interpreter import Interpreter
from convert_to_python import ToPythonInterpreter

def compile(code):
    l = Lexer(code)
    p = Parser(l)
    ast = p.program()
    SemanticAnalyzer(ast, False).visit()
    code = ToPythonInterpreter(ast).visit()
    return code

def runPseudocode(code, wantValues=False):
    l = Lexer(code)
    p = Parser(l)
    ast = p.program()
    SemanticAnalyzer(ast, False).visit()
    i = Interpreter(ast)
    i.visit()
    if wantValues:
        return i

text = '''
/*
hello
*/
DECLARE float: FLOAT
DECLARE real: REAL
DECLARE integer : INTEGER
DECLARE declared_array : ARRAY[2,8] OF STRING
DECLARE dlared_array : ARRAY[1:2+1,1:8] OF STRING
text <- 'hello'
declared_array[0 + 1][0] <- 'hi'
INPUT declared_array[1,2]
OUTPUT declared_array[1,2]
/* The python source to source compiler works with this
INPUT declared_array[1][2]
OUTPUT declared_array[1,2]()[1,2]
OUTPUT declared_array[1]()[2]*/

a <- 1 * 2 + 2 * 32 * 3
b <-  3
c <- b + a
OUTPUT b

OUTPUT TRUE
OUTPUT '### Loops Testing #########################'
d <- 0
FOR i <- 1 TO 10
    d <- d + 1
ENDFOR
OUTPUT d
WHILE d < 20 DO
    d <- d + 1
    OUTPUT d
ENDWHILE
OUTPUT d

OUTPUT '### Conditionals Testing #########################'
b <- 2
OUTPUT "b was"
OUTPUT b

IF b == 1  THEN
    a <- 1
ELSEIF b == 2 THEN
   a <- 2
ELSE
    a <- 2 + 2
ENDIF
OUTPUT "a is now"
OUTPUT a

OUTPUT '### Functions Testing #########################'

PROCEDURE hello(a, b, c)
    OUTPUT "## Hello is called ########"
    OUTPUT a
    OUTPUT b
    RETURN
    OUTPUT c
ENDPROCEDURE

FUNCTION hellofunc(a, b, c)
    OUTPUT "## hellofunc is called ########"
    OUTPUT "which calls hello(2, 3, 4)"
    CALL hello(2, 3, 4)
    OUTPUT "and returns hello" //, 1
    RETURN "hello"
ENDFUNCTION

CALL hello(1, 2, 3)
OUTPUT hellofunc(1, 2, 3)

'''

text1 = """
// Bubblesort Tech
// Notice how it still works even with inconsistencies in the FOR loops and Assignment statements
DECLARE a : ARRAY[3] OF INTEGER
a[0] = 1
a[1] = 0
a[2] = -1
a[3] = -2
length = 3

PROCEDURE BubbleSort(arr , length)
	exchanges <- True
	WHILE exchanges == True
  	    exchanges <- False
      	FOR i <- 0 TO length - 2
          	IF arr[i] > arr[i+1] THEN
                  	temp <- arr[i]
                  	arr[i] <- arr[i+1]
                  	arr[i+1] <- temp
          	    exchanges <- True
          	ENDIF
  	    NEXT i
	ENDWHILE
ENDPROCEDURE

CALL BubbleSort(a, length)
FOR i <- 0 TO length - 1
  OUTPUT a[i]
ENDFOR

"""
if __name__ == '__main__':
    #text = input('parse> ')
    code = text
    print(compile(code))
    print()
    print("--- Running code --------------------------------------------------------")
    print()
    i = runPseudocode(code, True)
    print(i.call_stack._records[0].members)

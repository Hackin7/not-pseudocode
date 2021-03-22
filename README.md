# not-pseudocode

This is a program that makes pseudocode Not Pseudocode. It converts Pseudocode meeting the A Level specifications to Python code. You can also run it I guess (with a non-existent standard library).

It is partially based off the standards [here](https://drive.google.com/file/d/17cYJY5ruEcjJh_Ve340oSCuwuAZdZ44e/view?usp=sharing)

The main aim is to be able to convert Pseudocode in A Level Papers (for me I'm from Singapore, so Singapore papers) into working code, and run it to test. However, being Pseudocode, the syntax is inconsistent, so it'll probably never be fully compatible. Nevertheless, for the core syntax, I've tried to make it compatible with the most common forms.

## Usage

### Python

Download the repository, edit the sample pseudocode (the variable `text`) in `python_src/main.py` and run it. It requires basically no dependencies

### Web interface

Access https://hackin7.github.io/not-pseudocode/.

## Syntax

### Comments
```
/*
Only multiline comments like this are supported for now
just Because
*/
```

### Variables

There are 3 main types of variables: `INTEGER`, `FLOAT`/`REAL` and `STRING`
You can also declare an `ARRAY` of 1 or 2 dimensions
```
DECLARE variable : STRING
/* Arrays are 1-indexed, but you can also use the 0-index (eg. one_d_array[0])*/
DECLARE one_d_array : ARRAY[8] OF INTEGER
DECLARE two_d_array : ARRAY[2, 8] OF FLOAT
DECLARE one_d_array_with_lower : ARRAY[1:8] OF INTEGER
DECLARE two_d_array_with_lower : ARRAY[1:2, 1:8] OF FLOAT

/* You can use <- or = */
variable = "random value"
unassigned_variable <- "value" /* Don't have to declare actually except for arrays */
two_d_array[1][1] = 1.1
two_d_array[1,1] = 1.1
```

### Arithmetic

For now there are only a few options
Operator | Explanation
--|--
`+`| Add
`-`| Subtract
`*`| Multiply
`/`| Divide
`DIV`| Quotient
`MOD`| Remainder
`=` or `==`| Equal
`!=` or `<>`| Not Equal
`<`| Less than
`<=`| Less than or equal to
`>`| Greater than
`>=`| Greater than or equal to
`NOT` | Not
`OR` | Or
`AND` | And
### Conditionals

```
b <- 1
IF b == 2 THEN
    a <- 1
ELSEIF b = 1 THEN
   a <- 2
ELSE
    a <- 2 + 2
ENDIF
OUTPUT a
```

You can omit the `THEN` if you Don't like it
```
b <- 1
IF b == 2
    a <- 1
ELSEIF b == 1
   a <- 2
ELSE
    a <- 2 + 2
ENDIF
OUTPUT a
```

This also works
```
b <- 1
IF b == 2
    a <- 1
ELSE IF b == 1
       a <- 2
ELSE
        a <- 2 + 2
ENDIF
OUTPUT a
```

But you may also want to look at this
```
b <- 1
IF b == 2
    a <- 1
ELSE
    CALL USELESS_FUNCTION()
    IF b == 1
        a <- 2
    ELSE
        a <- 2 + 2
    ENDIF
    /* You can insert code here and it'll run properly */
ENDIF
OUTPUT a
```
### Loops

```
d <- 0
FOR i <- 1 TO 10
    d <- d + 1
ENDFOR
OUTPUT d
WHILE d < 20 DO
    d <- d + 1
ENDWHILE
OUTPUT d
```

In the above example, you can also replace the `ENDFOR` with `NEXT i`, or omit the `DO` of the `WHILE` Loop

### Procedures & Functions

```
PROCEDURE hello(a: INTEGER, b, c)
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
    OUTPUT "and returns hello"
    RETURN "hello"
ENDFUNCTION

CALL hello(1, 2, 3)
OUTPUT hellofunc(1, 2, 3)
```

### Input Output
```
INPUT var_name
OUTPUT expression
OUTPUT expression1, expression2
```

### Other fun code to test around

Functions can return anything
```
FUNCTION test()
    DECLARE a : ARRAY[8] OF INTEGER
    a[1] <- 0
    RETURN a
ENDFUNCTION
OUTPUT test()[1]
```

Bubble Sort Example
```
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
        	FOR i <- 0 TO length - 1
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
```

Insertion Sort Example
```
PROCEDURE InsertionSort(arr, LENGTH)
    FOR i <- 1 TO LENGTH - 1
        key <- arr[i]
        curr <- i
        WHILE curr > 0 AND arr[curr - 1] >= key DO
            arr[curr] <- arr[curr - 1] // Shift up
            curr <- curr - 1
        ENDWHILE
        arr[curr] <- key
    NEXT i
ENDPROCEDURE
```

Binary Search
```
Size <- 5
DECLARE a : ARRAY[Size] OF INTEGER
a[1] = 1
a[2] = 2
a[3] = 3
a[4] = 4
a[5] = 5
Find <- 1


Low <- 1
High <- Size
Found <- -1

WHILE Low <= High AND Found == -1
    Mid <- (Low + High) DIV 2
    IF Find < a[Mid] THEN
        High <- Mid - 1
    ELSE IF a[Mid] < Find THEN
        Low <- Mid + 1
    ELSE
        Found <- Mid
    ENDIF
ENDWHILE

IF Found == -1 THEN
    OUTPUT "Not Found"
ELSE
    OUTPUT "Found at position ", Found
ENDIF
```

Semantic Analyser Checks
 - I'm too lazy to go through everything to see if all the data types line up, so make do with my crappy checks for now
```
DECLARE float: FLOT // Invalid Type
DECLARE float: FLOAT // Double Definition

PROCEDURE yes
    RETURN "value" //PROCEDURES CANNOT RETURN values
ENDPROCEDURE
```

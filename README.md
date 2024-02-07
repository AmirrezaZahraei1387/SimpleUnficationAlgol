# SimpleUnificationAlgol

## Goal
The goal of this program is creation of a simple
unification algorithm to receive two terms, and find
a substitution rule that best convert one to the other, or 
in other words make them equal. You can check out the test provided
to test the algorithm for some inputs provided there.

## Giving Input

Please run the "main.py" to run the project. Then you can give
your input based on the procedure it provides.

Below is a simple example that shows how to provide input:

```cmd
Important: Please make sure you use low letters for 
constants, and functions and upper case for variables

Please enter the expression: g(x, y , g(x, y, g(x, y), c))
Expression 1 captured successfully!

Please enter the expression: g(x, y , X)
Expression 2 captured successfully!

start unification ...
substitution rules are:
X = g(x,y,g(x,y),c)
```

## Build

You do not need to do any special thing to run the program.
Only run the main.py inside the same folder with other contents.

If you want to install the "UnifyOc" package for your internal use,
use "setup.py" to do it manually.
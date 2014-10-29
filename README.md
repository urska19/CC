CC
==
In repository there are two programs that were part of a homework for Computation and Computability subject in 2013/2014.

___

**Datoteke:**

- *naloga1.py* ... contains two bijective mappings: natural numbers and pairs of natural numbers and natural numbers and positive rational numbers

- *interpreter.py* ... interpreter for arbitrary BrainF*** (BF) program
- *fja.py* ... calculates the number of corresponding BF program
- *f2.py* ... calculates the BF program that corresponds to the number (only works for programs of length three and with no brackets)

___

**Guidence:**

- *naloga1.py* first argument is of the following form
  - "N-(N,N)" ... given numbers maps into a par of numbers
  - "(N,N)-N" ... given a pair of numbers maps in to a numbers
  - "N-Q+" ... given numbers maps into a pair of numbers that represent a fraction
  - "Q+-N" ... a fraction maps into its sequential number
and tells which function to choose, second (or third) are given arguments.
Example: python naloga1.py "N-Q+" 33


- *fja.py*  BF program is given as an argument in txt file
- *f2.py*  natural number is given as an argument

___

**Requirement**

Python

___

**Contact**

https://github.com/urska19

# Tutorial

This is a tutorial written by someone who does not know how to write a tutorial. Don't judge. 

## Introduction

This tutorial aims to introduce the *nanolisp* lisp dialect. Although it shares some features with other lisps, this dialect is meant to have a good amount of integration with Python. It is also meant to be very small (at the time of this writing, it is 35 lines long, well within the copy-paste-able limit). It does not have good error reporting, but I may add that later. Now, without further ado, let us start.

## Comparison with Other Lisps

As I said before, it has many commonalities with other lisps: it includes `define`, `lambda`, and basic operators. Notably, it lacks a macro system; you *can* define macros, but you cannot do it from the program itself. This is to ensure good practice; macros can only be written in Python. In addition, any Python built-in is also a nanolisp built-in. There is no way to circumvent this nor is there to redefine built-ins (this is currently a todo). You can also use any Python module from nanolisp or vice versa using the default `import` statement. Might as well start with that.

## Running Lisp Files

Let's say you have a nanolisp file like this in `testfile.scm`:
```scheme
(define x 5)
(define y 6)
```

How would you run it? There are two ways; you can run it from cmd-line or from a Python file. From command line, you would write it like this: `python -m nanolisp <filename>`. From a python file, you would write it like this:
```python
import nanolisp as nl
nl.init_loader()              # Now you can import any file that ends with the extension .scm
import testfile as fl
```

Note how you have to import nanolisp before you import the lisp module. And the beauty of this is that after you import the file, you can do this:
```python
print(fl.x, fl.y)
```

This prints out `5 6`.

## Macros

Macros are structures that enable a programmer to modify the structure of a running program. Although you cannot create macros in nanolisp, you can write them in python. Here's an example:
```python
def frominfix(match):
    return f"{x.group(2)} {x.group(1)} {x.group(3)}"

regex = r"(.+?) (.) (.+)"
nl.parsers.insert(0, (regex, frominfix))
```

`nl.parsers` is a constant which is a list of the parsers `nl.parse` uses to transform a nanolisp file into a Python tuple. As a slight example, here are some of the steps `nl.parse` uses to parse a file:

```python
(+ 1 2)
("+" "1" "2")             # Surround elements with quotes
("+", "1", "2",)          # Seperate elements with commas
(("+", "1", "2",),)       # Surround all elements with parentheses
```


# Nanolisp

The download page of many a language harbors deep senses of forboding, of evil lurking in its native lair. You feel
that the language is not a friend, that it means to harm you. You wonder what will happen when you click on the download
link.

But don't be scared. Nanolisp is a friend in a desert of programming languages. It can fit in a clipboard or an email. A file
or a project. Just 3 lines of code long, it really has earned its name. It only relies on standard, cross-platform modules. It
is an oasis for many a person.

## Installation

Copy and paste. *Et viola!* You have a complete nanolisp download! Python 3.8 or greater is needed to run the code. But I promise
you, it will be worth it.

The examples following this one will assume you have copy-pasted it into a file called `nl.py`.

## Basic Usage

Run `python3 nl.py` to open up the REPL. There, you can do many operations. Here is a sample session:

```
$ python3 nl.py
Welcome to Nanolisp 1.0.1!
> (+ 1 1)
2
> (define a 5)
> a
5
> (+ a 5)
10
> (define (inc n)
    (+ n 1))
> (inc 4)
5
> (exit)
$
```

As you can see, Nanolisp offers a full-featured repl. To run from a file is similarly simple: `python3 nl.py <filename>`. In fact, this repository
includes a test file, titled `schemetest.scm`, which implements an algorithm for square root and runs it on 10 (the algorithm itself was taken
from the seminal textbook on Scheme, [Structure and Interpretation of Computer Programs](https://mitpress.mit.edu/sites/default/files/sicp/index.html)).

## Advanced Usage

Although I made this for fun, I quickly realized that this could be applied to config files and similar goals. This leads to the fairly large topic
of a **Domain Specific Language (DSL)**. Nanolisp is designed to be extensible and easily so. Unfortunately, due to its complex implementation, it's
not extensible in all of its aspects.

**To be continued...**

## API

### Z (Environment)

Z is the variable used to store the environment. It has a custom type, but it was based off of Peter Norvig's implementation of the environment in
[lis.py](http://norvig.com/lispy.html). Why is it called Z? I have no idea.

### ev (evaluate)

Evaluate an AST (tuple of tuples).

### run

Run a string.

### rf (run file)

Open a file and run it (leaks memory, I guess)

### repl

Start the actual REPL, as opposed to the banner.

### parsers

The name is pretty misleading; this is a list of transformations applied to the lisp code to turn it into valid python code. Feel free to add elements to
it if you know what you're doing.

### initl (init loader)

Allows you to import scheme files.
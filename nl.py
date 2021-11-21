import base64 as b64,re,functools as ft,operator as op,collections as cl,sys
__version__,__doc__,env = '0.0.1','A pretty small lisp dialect', type('Env', (cl.ChainMap,), {'__getitem__': lambda self, s: r if (r := ft.reduce(lambda x, y: x or y, map(lambda d: d.get(s), self.maps))) else type('S', (str,), {})(s)})({
    'if': (mk_special := lambda fn: [setattr(fn, 'special', 1),fn][1])(lambda e, c, a, b: evaluate(a if evaluate(c, e) else b, e)),
    'display': print,
    'mk_str': lambda s: b64.b64decode(bytes(s, encoding='utf-8')).decode('utf-8'),
    'lookup': lambda s: env[s],
    'define': mk_special(lambda e, a, b: e.__setitem__(a[0] if (c := type(a) is tuple) else a, (lambda *s: evaluate(b, e.new_child(dict(zip(a[1:], s)))) if c else b))),
    'begin': lambda *a: a[-1],
    'exit': sys.exit,
    '+': op.add, '-': op.sub, '*': op.mul, '/': op.truediv, '^': pow, 'abs': abs, '<': op.le, '>': op.gt, '=': op.eq
})
special = [(x, x) for x in ['if', '-', '/', '>', '<', '=']] + [(f'\\{x}', x) for x in ['+', '*', '^']]
parsers = [('\n', ' '), (' +', ' '), (r'"(.*?)(?<!\\)"', lambda m: '(mk_str "' + b64.b64encode(bytes(m.group(1).replace(r'\"', '"'), encoding="utf-8")).decode("utf-8") + '")'), *[(f'(?<= |\(){x}(?= |\))', f'(lookup "{y}")') for x, y in [(x, x) for x in ['if', '-', '/', '>', '<', '=']] + [(f'\\{x}', x) for x in ['+', '*', '^']]], ('#t', 'True'), ('#f', 'False'), (' ', ', '), (r'\)', ',)')]

def topy(s):
    return eval(ft.reduce(lambda x, y: re.sub(*y, x), parsers, s), {}, env)

def evaluate(t, env):
    if type(t) in [list, tuple]:
        return (fn := evaluate(t[0], env))(*((env, *t[1:]) if hasattr(fn, 'special') else (evaluate(a, env) for a in t[1:])))
    elif type(t).__name__ == 'S':
        return env[t]
    else:
        return t

def run(s):
    return evaluate(eval(ft.reduce(lambda x, y: re.sub(*y, x), parsers, f'(begin {s.strip()})'), {}, env), env)
    # return evaluate(topy(f'(begin {s.strip()})'), env)
def runfile(filename): run(open(filename).read())
def repl(s="",p=f'Welcome to Nanolisp {__version__}!'):
    print(p)
    while True: 
        if (t := re.sub(r'"(.*?)(?<!\\)"', '', s := s + ' ' + input('  ' if s else '> '))).count('(') == t.count(')'): _, s = print(res) if (res := run(s)) is not None else 0, ""

runfile(sys.argv[1]) if len(sys.argv) > 1 else repl()

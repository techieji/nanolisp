(lambda f,o,r: [print(o(next(filter(lambda s: s.count('(') == s.count(')'), f.accumulate(map(
input, f.chain(['> '], f.repeat('  '))), lambda x,y: f'{x}\n{y}'))))) for _ in f.repeat(0)])(
__import__('itertools'), (lambda a,l,c,h,e,m,y:(lambda u: lambda s: a(eval(e.reduce(lambda s,
x: c.sub(*x, s),[('"(.*?)"', lambda r: 'σ'+h.b16encode(bytes(r.group(1),'utf-8')).decode()),(
f"({'|'.join(m.kwlist)}) " ,r'"ƒ\1",'), ("`(.*)`",r'"ƒ\1"'),('\s+',','),('\)',',)')],s),type(
'x',(dict,),{'__getitem__':lambda _,k:h.b16decode(bytes(k[1:],'u8')).decode()if k[0]=='σ'else
'ƒ' +k})()),u))(l.ChainMap({'ƒdefine': (ms:=lambda f: [setattr(f,'a',1), f][1])(lambda e,k,v:
e.__setitem__(k,run(v,e))),'ƒlambda':ms(lambda e,a,c:lambda*b:run(c,e.new_child(dict(zip(a,b)
)))),'ƒif':ms(lambda e,p,a,b:run(a if run(p, e)else b,e)),'ƒ<':y.lt,'ƒ+':lambda*x:sum(x),'ƒ-'
:lambda*x:x[0]-sum(x[1:]),'ƒ*':lambda*x:e.reduce(y.mul,x),'ƒ/':lambda*x:e.reduce(y.truediv,x)
,'ƒmacro':ms,'ƒcar':lambda x:x[0],'ƒcdr':lambda x:x[1:],'ƒdisplay':print,'ƒexit':exit})))(run
:=lambda s,e:(lambda f:f(*(e,)+s[1:]if hasattr(f, 'a')else map(lambda t:run(t,e),s[1:])))(run
(s[0],e))if type(s) == tuple else(e[s]if type(s) == str and s[0]=='ƒ'else s),*map(__import__,
'collections re base64 functools keyword operator'.split())),0) # => Perfection, consolidated

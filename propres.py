# Propositional model and resolution

# Literal: symbol or its negation  'X', '~X'
# Clause:  a list of literals (implied disjunction)
# CNF: a list of clauses (implied conjuction)

def isSymbol(x):
    return type(x) == str and len(x) == 1

def isConstant(x):
    return type(x) == bool

def isAtom(x):
    return isSymbol(x) or isConstant(x)

def isNegation(x):
    return type(x) == str and len(x) == 2 and x[0] == '~'

def isVariable(x):
    return type(x) == str and x[-1] == '_'

def opposite(x):
    if isNegation(x):
        return x[1:]
    return '~'+x

# Resolution theorem prover

def resolvePair(c1, c2):
    for lit1 in c1:
        for lit2 in c2:
            if lit2 == opposite(lit1):
                c1c = c1.copy()
                c2c = c2.copy()
                c1c.remove(lit1)
                c2c.remove(lit2)
                yield merge(c1c,c2c)

def resolveSet(c, done):
    for c1 in c:
        for c2 in c[c.index(c1)+1:]:
            if (c1, c2) in done:
                continue
            for ans in resolvePair(c1, c2):
                if ans in c:
                    continue
                yield (c+[ans],done+[(c1, c2)])

def resolveAll(c, done=[]):
    if [] in c:
        yield [c]
        return
    flag = False
    for (r0, done1) in resolveSet(c, done):
        flag = True
        for x in resolveAll(r0, done1):
            yield x
    if not flag:
        yield [c]
        
def merge(c1, c2):
    ans = c1.copy()
    for x in c2:
        if x in c1:
            continue
        ans.append(x)
    return ans

# Prettyprinters
# prints answers nicely

def showone(l):
    for x in l:
        print(x)
        
def show(l):
    hold = []
    for x in l:
        if x in hold:
            continue
        hold.append(x)
        showone(x)
        print()

# Example:  ((~T, M, E), (~S, ~E), T, S, ~M)

c1 = ['~T', 'M', 'E']
c2 = ['~S', '~E']
c3 = ['T']
c4 = ['S']
c5 = ['~M']

cs = [c1,c2,c3,c4,c5]


"""
Try:

>>>  ans = resolveAll(cs)

>>>  l = next(ans)

>>> show(l)

"""


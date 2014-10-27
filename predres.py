# CS364
# Predicate calculus resolution

from predunify import *

# One or more of these functions may need modification from the propositional calculus version, propres.py 

def resolvePair(c1, c2):
    for lit1 in c1:
        for lit2 in c2:
            u = lUnify(lit1, opposite(lit2))
            if u != "fail":
                if type(c1) == str and type(c2) == str:
                    c1c = c1.copy().remove(lit1)
                    c2c = c2.copy().remove(lit2)
                else:
                    l1 = list(c1)
                    l1.remove(lit1)
                    l2 = list(c2)
                    l2.remove(lit2)
                    c1c = tuple(l1)
                    c2c = tuple(l2)
                c1c = applySubst(c1c, u)
                c2c = applySubst(c2c, u)
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
            yield [c]+x
    if not flag:
        yield [c]

def merge(c1, c2):
    ans = list(c1)
    for x in c2:
        if x in c1:
            continue
        ans.append(x)
    return tuple(ans)

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

# Examples

cx0 = [("~B", 'Z'), ("~A", "X", "B")]
cx1 = [("B", ("f", "Y")), ("~C", "X", "Y", "Z")]
cx2 = [("A", ("f", "a"), "Y")]
cx3 = [("C", ("f", "a"), "b", "Z")]

cx = [cx0, cx1, cx2, cx3]

# This one is from Coppin, p. 236

c1 = [('C', 'a')]
c2 = [('~F', 'Y'), ('L', 'a', 'Y')]
c3 = [('~C', 'X'), ('~F', 'Y'), ('~G', 'Y'), ('~L', 'X', 'Y')]
c4 = [('~F', 'X'), ('~M', 'c', 'X'), ('~C', 'Y'), ('L', 'Y', 'X')]
c5 = [('F', 'b')]
c6 = [('M', 'c', 'b')]
c7 = [('G', 'b')]

cs = [c1,c2,c3,c4,c5,c6,c7]


"""
Try:

>>>  ans = resolveAll(cx)

>>>  l = next(ans)

>>> show(l)

"""

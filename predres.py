# CS364
# Predicate calculus resolution

from predunify import *

# Resolution theorem prover

def resolvePair(c1, c2):
    for pred1 in c1:
        for pred2 in c2:
            sub = aUnify(pred1, opposite(pred2))
            if sub != "fail":
                c1r = c1.copy()
                c1r.remove(pred1)
                c2r = c2.copy()
                c2r.remove(pred2)
                c1sub = applyS(c1r, sub)
                c2sub = applyS(c2r, sub)
                yield merge(c1sub,c2sub)

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

# we couldn't get predunify's applySubst() to work, so we wrote this:
def applyS(preds, sub):
    retval = []
    for pred in preds:
        l = []
        for e in pred:
            if e in sub.keys():
                l.append(sub[e])
            else:
                l.append(e)
        retval.append(tuple(l))
    return retval


# CS364
# Predicate calculus representation unification and substitution

import string

### Predicate Calculus model
# Symbols: "_" or alphanumeric strings beginning with a letter
# Constants:  numbers or numerical strings or symbols beginning with lower case letter
# Variables:  symbolsF beginning with upper case letter
# FunCall:    tuple with symbol in leftmost position; remaining positions are terms
#             eg., ('f', 'X', 'a')
#             FunCall can be used to identify both predicates and functions
# Negatives:  eg., ('~P', 'a', 'b') or '~X'
# Literal:    Variable or predicate, or its negation

def isSymbol(x):
    if type(x) != str:
        return False
    if type(x)==str and x != "_" and x[0] != "~" and not (x[0] in string.ascii_letters):
        return False
    for c in x[1:]:
        if not (c in string.ascii_letters or c in string.digits):
            return False
    return True

def isConstant(x):
    if type(x) == int or type(x) == float or isIntString(x) or isFloatString(x):
        return True
    return isSymbol(x) and x[0] in string.ascii_lowercase

def isVariable(x):
    if type(x) == int or type(x) == float:
        return False
    return isSymbol(x) and x[0] in string.ascii_uppercase

def isPred(x):
    return isFunCall(x)

def isTerm(x):
    return isVariable(x) or isConstant(x) or isFunCall(x)

def isFunCall(x):
    if type(x) == tuple:
        if isSymbol(x[0]):
            for v in x[1:]:
                if not isTerm(v):
                    return False
            return True

def isLiteral(x):
    return isVariable(x) or isPred(x)
        
# isNegation identifies a negative literal (i.e. variable or predicate)

def isNegation(x):
    if type(x) == str:
        x0 = x[0]
        x1 = x[1:]
        return x0 == '~' and isVariable(x1)
    elif isPred(x):
        return x[0][0] == '~'

# isIntString and isFloatString are help functions used to identify
#  numerical strings

def isIntString(s):
    try:
        t = int(s)
        return True
    except:
        return False

def isFloatString(s):
    try:
        t = float(s)
        return True
    except:
        return False

#####
### Substitutions
# subsititutions are modeled as dictionaries

# newSubst creates a new empty substitution

def newSubst():
    return dict()

# applySubst(e, s) substitutes in e all occurences of
#  the variables in s with their values

def applySubst(e, s):
    def replace(v):
        return s[v] if v in s.keys() else v
    return visitVars(e, replace)

# composeSubst(s1, s2) = s1 o s2, the composition of s1 and s2

def composeSubst(s1, s2):
    s3 = newSubst()
    for k in s1.keys():
        v = applySubst(s1[k], s2)
        if k != v:
            s3[k] = v
    for k in s2.keys():
        if not k in s3.keys():
            s3[k] = s2[k]
    return s3

# help functions

# visitVars(e, f)
# traverses e and applies f to every variable found in e

def visitVars(e, f):
    if isVariable(e):
        return f(e)
    e1 = isNegation(e)
    if e1:
        return opposite(visitVars(opposite(e), f))
    if isFunCall(e):
        return funcify(e[0], list(map(lambda x:visitVars(x, f), e[1:])))
    return e

# opposite(x) returns the representation of the negative of x

def opposite(x):
    if type(x)==str:
        if isNegation(x):
            return x[1:]
        return "~"+x
    if isNegation(x):
        return tuple([x[0][1:]]+list(x[1:]))
    return tuple(["~"+x[0][0]]+list(x[1:]))

# funcify creates a function call (i.e. function and args) for a predicate or function

def funcify(f, args):
    return tuple([f]+args)

####
### Unification

# lUnify(l0, l1)
#  unifies literals

def lUnify(l0, l1):
    if isNegation(l0) and isNegation(l1):
        return aUnify(opposite(l0), opposite(l1))
    if isNegation(l0) or isNegation(l1):
        return 'fail'
    return aUnify(l0, l1)

# aUnify(p0, p1)
#  unifies atomic sentences p0 and p1
#    fails unless predicate symbols are identical and same number of args
#    otherwise calls tUnifyList to unify the args

def aUnify(p0, p1):
    if not isPred(p0) or not isPred(p1) or len(p0) != len(p1) or (p0[0] != p1[0]):
        return "fail"
    return tUnifyList(list(p0[1:]), list(p1[1:]))

# tUnifyList(l0, l1)
#  unifies 2 lists of terms of the same length
#  starting with an empty substitution s:
#  1. if l0 (and l1) are empty, return unwind(s)
#  2. apply s to the first terms of l0 and l1 and use tUnify to get s1
#  3. fail if s1 == fail
#  4. otherwise recur with s = s o s' on the rest of l0 and l1

def tUnifyList(l0, l1):
    def hUnifyList(l0, l1, s0):
        if len(l0) == 0:
            return unwind(s0)
        l0s = applySubst(l0[0], s0)
        l1s = applySubst(l1[0], s0)
        s1 = tUnify(l0s, l1s)
        if s1 == "fail":
            return "fail"
        return hUnifyList(l0[1:], l1[1:], composeSubst(s1, s0))
    return hUnifyList(l0, l1, newSubst())

# tUnify(t0, t1)
#  unifies t0 and t1 to produce substitution s
#  if t0 is a variable, return {t0: t1} (unless t1 is a function and t0 occurs in t1; in which case fail)
#  if t0 is a constant and t1 is a variable, return {t1: t0}; otherwise fail
#  if t0 is a function:
#     if t1 is a variable and t1 does not occur in t0, return {t1: t0}
#     if t1 is a function with same function symbol and length, return tUnifyList applied to the args
#     otherwise fail

def tUnify(t0, t1):
    if isVariable(t0):
        if isVariable(t1) or isConstant(t1) or (isFunCall(t1) and not occursIn(t0, t1)):
            return dict({t0:t1})
        return "fail"
    if isConstant(t0):
        if isVariable(t1):
            return dict({t1:t0})
        if isConstant(t1) and t0 == t1:
            return newSubst()
        return "fail"
    if isFunCall(t0):
        if isVariable(t1) and not occursIn(t1, t0):
            return dict({t1:t0})
        if isConstant(t1):
            return "fail"
        if isFunCall(t1) and len(t0) == len(t1) and t0[0] == t1[0]:
            return tUnifyList(list(t0[1:]), list(t1[1:]))
        return "fail"

# occursIn(v, t)
#  return true if variable v occurs in term t; false otherwise
            
def occursIn(v, t):
    if v == t:
        return True
    if isVariable(t) or isConstant(t):
        return False
    for x in t:
        if occursIn(v, x):
            return True
    return False

# unwind(s)
#  unwind guarantees that all bound variables are replaced by their
#  values in the values of other bindings; it does this by repeated self-composition
#  until no further changes are detected

def unwind(s):
    s1 = s
    while True:
        s2 = composeSubst(s1, s)
        if s2 == s1:
            return s1
        s1 = s2
        

# Try aUnify on this pair

p1 = ("foo", "Z", ("f", "X"), "Z")
p2 = ("foo", ("f", "a"), "Y", "Y")




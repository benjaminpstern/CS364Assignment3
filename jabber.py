# Jabber.py
# CS 364 Assignment 3
# problem 5b.
# Cole Peppis and Ben Stern

from predres import *

b = [[('~shark','X'),('certainWFO','X')],[('~fish','Y'),('canDanceM','Y'),('contemptible','Y')],[('~fish','Z'),('has3RT','Z'),('~certainWFO','Z')],[('~fish','W'),('shark','W'),('~kindToC','W')],[('~fish','V'),('~heavy','V'),('~canDanceM','V')],[('~fish','U'),('~has3RT','U'),('~contemptible','U')],[('fish','t')],[('heavy','t')],[('kindToC','t')]]
# since the fish(X) occurs in all of the clauses and isn't necessary for the resolution, we removed it:
c = [[('~shark','X'),('certainWFO','X')],[('canDanceM','Y'),('contemptible','Y')],[('has3RT','Z'),('~certainWFO','Z')],[('shark','W'),('~kindToC','W')],[('~heavy','V'),('~canDanceM','V')],[('~has3RT','U'),('~contemptible','U')],[('heavy','t')],[('kindToC','t')]]

ans = resolveAll(c)
l = next(ans)

def main():
    show(l)

main()

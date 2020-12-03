MPH    = 60 # minutes per hour
notes  = [] # arrival times
from collections import defaultdict
lookup = defaultdict(int) # gfg
keys   = [] # distinct arrival times
###                        *
###        *               *
###        * *     *       *       *
### |0|1|2|3|4|5|6|7|8|9|a|b|c|d|e|f|..
###        i(nitial)       n(ext)
###
###              *                           *
###  *   *   *   *   *   *   *   *   *   *   *   *   *   *   *
### [0,  3,  5,  13, 15, 21, 26, 27, 29, 37, 39, 45, 51, 52, 53]
###
### i - init arival time
### n - next arival time
def conseq(i, n):
    """"""
    delta = (n - i)
    return range(n + delta, MPH, delta)
def isit(i, n):
    ''' thatz '''
    for k in conseq(i, n):
        if not (k in keys): return False
        if not lookup[k]: return False
    return True
def mark(i, n):
    """ """
    for k in (i, n, *conseq(i, n)):
        lookup[k] -= 1
def unmark(i, n):
    ''' /'''
    for k in (i, n, *conseq(i, n)):
        lookup[k] += 1
def iniz():
    """ initialize """
    with open('INPUT.5') as f:
        notes[:] = map(int, f.readline().split())
    # lookup dict
    for t in notes: lookup[t] += 1
    keys[:] = list(lookup.keys())
def next_note(j):
    ''' '''
    while True: # thats the loop
        j += 1
        if not (j < len(notes)): return -1
        t = notes[j]
        if (0 < lookup[t]): return j
def next_keys(i):
    """***"""
    return keys[(1 + keys.index(i)):]
# some data structure:
route = [] # (i, n) stack
class Flag(Exception): pass
def bforce(j):
    """"""
    # ar ve don?
    if (-1 == j): raise Flag()
    i = notes[j] # initial arrival time
    # next arrival loof
    for n in next_keys(i):
        # route ck
        if not isit(i, n): continue
        # register route
        route.append((i, n))
        # discard from lookup table
        mark(i, n)
        # click next
        bforce(next_note(j))
        # postvisit
        unmark(i, n)
        route.pop()
VERBOSE = 1
DEBUG   = 0
if __name__ == '__main__':
    if DEBUG: import pdb; pdb.set_trace()
    iniz()
    if VERBOSE:
        print("notes:", notes)
        print("lookup:", dict(lookup))
        print("keys:", keys)
    try:
        bforce(0)
    except Flag:
        print(*route, sep='\n')
################################################################
# log:

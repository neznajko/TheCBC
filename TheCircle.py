#  1  3 10  2  5
#  1  5  2 10  3
#  2  4  9  3  5
#  2  5  3  9  4
class Flag(Exception): pass
stk = []
# j  - levl
# k  - minimum coin value
# mx - maximum bounds
def ntuple(j, k, mx, coins):
    ''''''
    if j: mn = coins[j - 1] + 1
    else:
        mn = k
        stk[:] = []
    for i in range(mn, mx[j] + 1):
        coins[j] = i
        if j == (len(coins) - 1):
            stk.append(tuple(coins))
        else:
            ntuple(j + 1, k, mx, coins)
def poke(ls, j): return ls[:j] + ls[(j + 1):]
Dict = {}
def perm(ls):
    if not ls: return [[]]  # empty
    bf = []
    for j in range(len(ls)):
        ls2 = poke(ls, j)
        tpl = tuple(ls2)    # «dynamic programming»
        if tpl in Dict:     #
            bf2 = Dict[tpl] #
        else:               #
            bf2 = perm(ls2) #
            Dict[tpl] = bf2 #
        for p in bf2:
            bf.append(p + [ls[j]])
    return bf                    
def summarize(coins):
    '''```'''"""do the math"""
    n = len(coins)
    aux = []
    for j in range(n):
        for k in range(n - 1):
            Sk = 0
            for i in range(k + 1):
                Sk += coins[(j + i)%n]
            aux.append(Sk)
    aux.append(sum(coins))
    return aux
def conseq(m, coins):
    """ Count Consecutive Sums """
    aux = summarize(coins)
    aux = mergesort(aux)
    if not m in aux: return 0
    n = 1 # counter
    for j in range(aux.index(m) + 1, len(aux)):
        d = aux[j] - aux[j - 1]
        if   d == 0: continue
        elif d == 1: n += 1
        else       : break
    return n
def maxconseq(m, coins):
    ''' coins are ordered tuples from stk '''
    k = coins[0] # [Ok] this is fixed
    mx   = 0  # max
    pstk = [] # 
    for p in perm(coins[1:]):
        p = [k, *p]
        n = conseq(m, p)
        if mx < n:
            mx = n
            pstk[:] = [p]
        elif mx == n:
            pstk.append(p)
    return (mx, pstk)
def merge(left, ryte):
    ''''''
    if not left: return ryte
    if not ryte: return left
    if ryte[-1] < left[-1]:
        n = left.pop()
    else:
        n = ryte.pop()
    m = merge(left, ryte)
    m.append(n)
    return m
def mergesort(ls):
    """"""
    if len(ls) < 2: return ls
    n = len(ls) // 2
    return merge(mergesort(ls[:n]), mergesort(ls[n:]))
from math import (log2, ceil)
def maxbound(m, n):
    """2"""
    ls = [2**ceil(log2(m))]
    for _ in range(1, n):
        ls.append(2*ls[-1])
    return ls
def dothemath(n, m, k):
    """ that'z """
    mx = maxbound(m, n)
    ntuple(0, k, mx, [0]*len(mx))
    mx2   = 0
    perms = []
    for coins in stk:
        conseq = maxconseq(m, coins)
        if mx2 < conseq[0]:
            mx2 = conseq[0]
            perms[:] = [conseq[1]]
        elif mx2 == conseq[0]:
            perms.append(conseq[1])
    return mx2, perms        
class Testo:
    ''' _es_ing =es=ing 4es4ing '''
    def ntuple():
        k = 1
        mx = (1, 2, 4, 8, 16)
        coins = [0]*len(mx)
        ntuple(0, k, mx, coins)
        print(*stk, sep='\n')
    def perm():
        p = perm((0, 1, 2, 3, 4))
        print(*p, len(p), sep='\n')
        print("Keys:", *Dict, sep='\n')
    def summarize():
        coins = [2, 3, 7, 4]
        print(*summarize(coins), sep='\n')
    def conseq():
        coins = (1, 3, 10, 2, 5)
        m = 2
        print(conseq(m, coins))
    def merge():
        print(merge([1, 5, 10], [5, 17]))
    def mergesort():
        print(mergesort([15, 13, 8, -5, 1]))
    def maxbound():
        print(maxbound(2, 5))
    def maxconseq():
        m = 2
        coins = (1, 2, 3, 5, 10)
        print(maxconseq(m, coins))
    def dothemath():
        conseq = dothemath(4, 2, 1)
        print(conseq[0])
        print(*conseq[1], sep='\n')
#  __    __     __    __
if __name__ == '__main__':
    Testo.dothemath()
################################################
# log:
# > n-tuple generation
#    * backtrack
# > permutation generation
#    * dynamic programming
# > merge sort
#    * divide and conquer
# > uBaG7o mo He ce nycHa no gkanaHku ctc Tas
#    * Furapka?

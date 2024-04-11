import sys
import math
from collections import deque
import random


class Map(object):
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.m =[['?' for x in range(w)] for x in range(h)]
        self.sight = 2
    def __getitem__(self, i):
        return self.m[i]
    def __contains__(self, n):
        r, c = n
        return (r>=0 and r<self.h and c>=0 and c<self.w)
    def adj(self, r, c):
        dirs = [["LEFT", "RIGHT"], ["UP","DOWN"]]
        for i, off in enumerate((-1,1)):
            yield (self.m[r][c + off], (r,c+off), dirs[0][i])
            yield (self.m[r + off][c], (r+off,c), dirs[1][i])
    def hor(self, r, c):
        h = []
        for i in range(r-self.sight, r+self.sight+1):
            for j in range(c-self.sight, c+self.sight+1):
                n = (i,j)
                if n in self:
                    h.append(n)
        return h
                    
        

def main():
    # r: number of rows.
    # c: number of columns.
    # a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
    r, c, a = [int(i) for i in input().split()]
    
    m = Map(c,r)
    
    print("h,w:", (m.h,m.w), file=sys.stderr)
     
    # possible states:
    # 'explore' looking for C
    # 'stuck' going to closest ?
    # 'control' going to C
    # 'escape' going back to T
    state = 'explore'
    cLoc = None # control room location
    
    # game loop
    while True:
        # kr: row where Kirk is located.
        # kc: column where Kirk is located.
        kr, kc = [int(i) for i in input().split()]
        for i in range(m.h):
            row = input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
            print(row, file=sys.stderr)
            for j, v in enumerate(row):
                m[i][j] = v

        print("kr,kc:", (kr,kc), file=sys.stderr)
        for r in m[kr-m.sight:kr+m.sight+1]:
            print(" ".join(r[kc-m.sight:kc+m.sight+1]), file=sys.stderr)
        
        print("state:", state, file=sys.stderr)

        if state == 'explore':
            action = None
            
            if cLoc is None:
                cLoc = loc(m.hor(kr,kc), m, 'C')
            if not cLoc is None:
                cr, cc = cLoc
                pathT = treeBfs(cr, cc, m, lambda node,v: v != 'T')
                if not pathT is None and pathT.h <= a:
                    state = 'control'
                    pathC = treeBfs(kr, kc, m, lambda node,v: v != 'C')
                    action = pathC.action
                    pathC = pathC.pChild
                    
            if action is None:
                cells = [c for c in m.adj(kr,kc)]
                random.shuffle(cells)
                
                vcells = []
                for v, n, d in cells:
                    if v == ".":
                        r,c = n
                        vcells.append([(r,c), d, count(m.hor(r,c), m, '?')])
                            
                vcells.sort(key=lambda c: c[-1], reverse=True)
                print("vc:", vcells, file=sys.stderr)
                
                if vcells[0][-1] > 0:
                    action = vcells[0][1]
                else:
                    print("got stuck", file=sys.stderr)
                    def step(node, v):
                        return v != '?'
                    pathTree = treeBfs(kr,kc,m,step)
                    state = 'stuck'
                    action = pathTree.action
                    pathTree = pathTree.pChild
        elif state == 'stuck':
            action = pathTree.action
            pathTree = pathTree.pChild
            if pathTree.h <= 1:
                print("unstuck", file=sys.stderr)
                state = 'explore'
            else:
                print("still stuck", file=sys.stderr)
        elif state == 'control':
            if pathC is None:
                state = 'escape'
                action = pathT.action
                pathT = pathT.pChild
            else:
                action = pathC.action
                pathC = pathC.pChild
        elif state == 'escape':
            action = pathT.action
            pathT = pathT.pChild
    
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)
    
        # Kirk's next move (UP DOWN LEFT or RIGHT).
        print(action)
   
   
# returns the coords of the first occurence of s in m at the coords in l
# returns None if s is not found
def loc(l, m, s):
    n = None
    for r,c in l:
        if m[r][c] == s:
            n = (r,c)
            break
    return n
    

# counts the occurences of s in m at the coords in l    
def count(l, m, s):
    n = 0
    for r,c in l:
        if m[r][c] == s:
            n+=1
    return n
    
    
def treeBfs(r,c,m,step):
    treeNodes = {}
    root = Tree()
    treeNodes[(r,c)] = root
    def treeStep(t,n,v,d):
        father = treeNodes[t]
        child = Tree(father, d)
        treeNodes[n] = child
        stepRes = step(child, v)
        if not stepRes:
            child.h = 1
            while not father is None:
                father.pChild = child
                father.h = child.h + 1
                child = father
                father = father.father
        return stepRes
    bfs(r,c,m,treeStep)
    return root.pChild
        
    
def bfs(r,c,m,step):
    toLook = deque([(r,c)])
    explored = set([(r,c)])
    while len(toLook) > 0:
        r,c = t = toLook.popleft()
        for v, n, d in m.adj(r,c):
            if not n in explored:
                explored.add(n)
                if v == '.' or v == 'T':
                    toLook.append(n)
                if not step(t, n, v, d):
                    return
    
    
class Tree(object):
    def __init__(self, father=None, action=None):
        self.father = father
        self.action = action
        if not father is None:
            father.addChild(self)
        self.children = set()
        self.pChild = None # prodigal child, the most useful one
    def addChild(self, child):
        self.children.add(child)
    
    
main()

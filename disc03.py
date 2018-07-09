# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 23:59:26 2017

@author: ZY
"""

def tree(root, branches=[]):
    return [root]+list(branches)

def root(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_leaf(tree):
    return not branches(tree)

t=tree(1,
       [tree(3,
             [tree(4),
              tree(5),
              tree(6)]),
       tree(2)])


#question 3.1.1
def square_tree(t):
    if is_leaf(t):
        return [root(t)**2]
    else:
        newtree=[root(t)**2]
        for branch in branches(t):
            newtree=newtree+[square_tree(branch)]
        return newtree
 
squaretree=square_tree(t)

#question 3.1.2
def height(t):
    if is_leaf(t):
        return 0
    else:
        my_max=0
        for branch in branches(t):
            my_max=max(height(branch),my_max)
        return my_max+1
    
ht=height(t)

#question 3.1.3
def tree_max(t):
    if is_leaf(t):
        return root(t)
    else:
        my_max=-999
        for branch in branches(t):
            my_max=max(tree_max(branch),my_max)
        return my_max
    
maxtree=tree_max(t)



#question 3.2.1
tree321=[2,[7,[3],[6,[5],[11]]],[15]]
def find_path(tree,x):
    if is_leaf(tree) and root(tree)==x:
        return [x]
    elif not is_leaf(tree):
        for branch in branches(tree):
            ans=find_path(branch,x)
            if ans and ans[-1]==x:
                return [root(tree)]+ans
        
findpath=find_path(tree321,5)

#question 3.2.2
def prune(t,k):
    if k==0:
        return [root(t)]
    else:
        ans=[root(t)]
        for branch in branches(t):
            ans=ans+[prune(branch,k-1)]
        return ans
    
prunetree=prune(tree321,2)

#question 3.2.3
def hailstone_tree(n,h):
    if h==0:
        return [n]
    elif h>0:
        if (n-1) % 3 == 0:
            return [n]+[hailstone_tree(n*2, h-1)]+[hailstone_tree((n-1)//3,h-1)]
        else:
            return [n]+[hailstone_tree(n*2, h-1)]
        
hailstonetree=hailstone_tree(8,3)
    
    
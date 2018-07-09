from lab07 import *

# Q6
def reverse_other(t):
    """Reverse the roots of every other level of the tree using mutation.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(5, [Tree(7), Tree(8)]), Tree(6)]), Tree(3)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(3, [Tree(5, [Tree(8), Tree(7)]), Tree(6)]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if not t.is_leaf():
        ans=[]
        x=len(t.branches)
        for branch in t.branches:
            ans.append(branch.root)
        for branch in t.branches:
            branch.root=ans[x-1]
            x -= 1
            for next_branch in branch.branches:
                reverse_other(next_branch)
        
    

# Q7
def cumulative_sum(t):
    """Mutates t where each node's root becomes the sum of all entries in the
    corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if not t.is_leaf():
        ans = t.root
        for branch in t.branches:
            cumulative_sum(branch)
            ans += branch.root
        t.root = ans

# Q8
def deep_map_mut(fn, link):
    """Mutates a deep link by replacing each item found with the
    result of calling fn on the item.  Does NOT create new Links (so
    no use of Link's constructor)

    Does not return the modified Link object.

    >>> link1 = Link(3, Link(Link(4), Link(5, Link(6))))
    >>> deep_map_mut(lambda x: x * x, link1)
    >>> print_link(link1)
    <9 <16> 25 36>
    """
    "*** YOUR CODE HERE ***"
    if not link.rest == Link.empty:
        if isinstance(link.first, int):
            link.first=fn(link.first)
        elif isinstance(link.first, Link):
            deep_map_mut(fn, link.first)
        deep_map_mut(fn, link.rest)
    else:
        if isinstance(link.first, int):
            link.first=fn(link.first)
        elif isinstance(link.first, Link):
            deep_map_mut(fn, link.first)

# Q9
def has_cycle(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    if link.rest == Link.empty:
        return False
    elif link.rest.first<link.first:
        return True
    else:
        return has_cycle(link.rest)

def has_cycle_constant(link):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"

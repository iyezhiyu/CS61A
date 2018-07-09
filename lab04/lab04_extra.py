from lab04 import *

# Q12
def flatten(lst):
    """Returns a flattened version of lst.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    "*** YOUR CODE HERE ***"
    ans=[]
    for i in lst:
        if type(i) == list:
            ans=ans+flatten(i)
        else:
            ans=ans+[i]
    return ans
    

# Q13
def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    ans=[]
    now1=0
    now2=0
    while now1<len(lst1) or now2<len(lst2):
        if now1<len(lst1) and now2<len(lst2):
            if lst1[now1]<lst2[now2]:
                ans=ans+[lst1[now1]]
                now1+=1
            else:
                ans=ans+[lst2[now2]]
                now2+=1
        elif now1<len(lst1):
            ans=ans+[lst1[now1]]
            now1+=1
        else:
            ans=ans+[lst2[now2]]
            now2+=1
    return ans

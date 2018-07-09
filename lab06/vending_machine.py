def vending_machine(snacks):
    """Cycles through list of snacks.

    >>> vender = vending_machine(('chips', 'chocolate', 'popcorn'))
    >>> vender()
    'chips'
    >>> vender()
    'chocolate'
    >>> vender()
    'popcorn'
    >>> vender()
    'chips'
    >>> other = vending_machine(('brownie',))
    >>> other()
    'brownie'
    >>> vender()
    'chocolate'
    """
    "*** YOUR CODE HERE ***"
    i=-1
    def my_cycle():
        nonlocal i
        i=(i+1)%len(snacks)
        return snacks[i]
    return my_cycle

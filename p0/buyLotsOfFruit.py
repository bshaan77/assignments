#!/usr/bin/env python3

"""
Based off of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

To run this script, type:

  python3 buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

FRUIT_PRICES = {
    'apples': 2.00,
    'oranges': 1.50,
    'pears': 1.75,
    'limes': 0.75,
    'strawberries': 1.00
}

def buyLotsOfFruit(orderList):
    total = 0
    for n in orderList:
        if n[0] not in FRUIT_PRICES:
            return None
        else:
            total += n[1] * FRUIT_PRICES[n[0]]
    return total

    """
    orderList: List of (fruit, weight) tuples

    Returns cost of order
    """

    # *** Your Code Here ***

    return None

def main():
    orderList = [
        ('apples', 2.0),
        ('pears', 3.0),
        ('limes', 4.0)
    ]

    print("Cost of %s is %s." % (orderList, buyLotsOfFruit(orderList)))

if __name__ == '__main__':
    main()

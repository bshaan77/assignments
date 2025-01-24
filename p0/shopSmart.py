#!/usr/bin/env python3

"""
Based of of: http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders: [('apples', 1.0), ('oranges', 3.0)] best shop is shop1.
For orders: [('apples', 3.0)] best shop is shop2.
"""

import shop

def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPound) tuples
    fruitShops: List of FruitShops
    """

    total = {shop: 0 for shop in fruitShops}
    
    for shop in fruitShops:
        for n in orderList:
            if n[0] not in shop.fruitPrices:
                return None
            else:
                total[shop] += n[1] * shop.fruitPrices[n[0]]

    return min(total, key=total.get)

def main():
    dir1 = {
        'apples': 2.0,
        'oranges': 1.0
    }

    dir2 = {
        'apples': 1.0,
        'oranges': 5.0
    }

    shop1 = shop.FruitShop('shop1', dir1)
    shop2 = shop.FruitShop('shop2', dir2)

    shops = [shop1, shop2]

    orders = [('apples', 1.0), ('oranges', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

    orders = [('apples', 3.0)]
    print("For orders: %s the best shop is %s." % (orders, shopSmart(orders, shops).getName()))

if __name__ == '__main__':
    main()

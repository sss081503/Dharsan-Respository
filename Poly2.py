#  File: Poly.py

#  Description: takes polynomials as linked lists and adds and multiplies them

#  Student Name: Joseph Mikhail

#  Student UT EID: jym436

#  Partner Name: Surendra Anne

#  Partner UT EID: sva398

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 11/03/22

#  Date Last Modified: 11/03/22

import sys


class Link(object):
    def __init__(self, coeff=1, exp=1, next=None):
        self.coeff = coeff
        self.exp = exp
        self.next = next

    def __str__(self):
        return '(' + str(self.coeff) + ', ' + str(self.exp) + ')'


class LinkedList(object):
    def __init__(self):
        self.first = None

    def get_num_terms(self):
        count = 0
        current = self.first
        while (current.next != None):
            current = current.next
            count += 1
        return count

    # add an item at the beginning of the list
    def insert_first(self, coeff, exp):
        new_link = Link(coeff, exp)

        new_link.next = self.first
        self.first = new_link

    # add an item at the end of a list
    def insert_last(self, coeff, exp):
        new_link = Link(coeff, exp)
        current = self.first

        if (current == None):
            self.first = new_link
            return

        while (current.next != None):
            current = current.next
        current.next = new_link

    # looks for link of desired exponent, if there are none it returns none
    # if found, returns current coefficient
    def find(self, exp):
        current = self.first

        # special case if link is empty
        if (current == None):
            return None

        while (current.exp != exp):
            # checks if you are at end
            if (current.next == None):
                return None
            else:
                current = current.next

        # returns link with data that you are looking for
        return current.coeff

    # keep Links in descending order of exponents
    def insert_in_order(self, coeff, exp):
        new_link = Link(coeff, exp)
        current = self.first
        previous = self.first

        # case if list is empty (may not need this)
        if (current == None):
            # print('empty')
            self.first = new_link
            return

        for i in range(self.get_num_terms() + 1):
            if (current.exp <= exp):
                break
            previous = current
            current = current.next

        if current == self.first:
            # print('first')
            self.insert_first(coeff, exp)
        elif current == None:
            # print('last')
            self.insert_last(coeff, exp)
        else:
            # print('middle')
            new_link.next = previous.next
            previous.next = new_link

    def delete_link(self, exp):
        previous = self.first
        current = self.first

        # checks if list is empty
        if (current == None):
            return None

        while current.exp != exp:
            if current.next == None:
                return None
            else:
                previous = current
                current = current.next

        if (current == self.first):
            self.first = current.next
        else:
            previous.next = current.next

        return current.exp

    # add polynomial p to this polynomial and return the sum
    def add(self, p):
        current = self.first
        sum = LinkedList()
        while (current != None):
            prev = sum.find(current.exp)
            if (prev == None):
                sum.insert_in_order(current.coeff, current.exp)
            else:
                sum.delete_link(current.exp)
                sum.insert_in_order(current.coeff + prev, current.exp)
            current = current.next

        current = p.first
        while (current != None):
            prev = sum.find(current.exp)
            if (prev == None):
                sum.insert_in_order(current.coeff, current.exp)
            else:
                sum.delete_link(current.exp)
                sum.insert_in_order(current.coeff + prev, current.exp)
            current = current.next

        return sum

    # multiply polynomial by single term
    # returns new polynomial
    def mult_sing(self, one):
        mult = LinkedList()
        current = self.first
        while (current != None):
            mult.insert_in_order(current.coeff * one.coeff, current.exp + one.exp)
            # current.coeff = current.coeff * one.coeff
            # current.exp = current.exp + one.exp
            current = current.next

        return mult

    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        product = LinkedList()
        current = self.first
        factors = []

        while (current != None):
            # factors.append(p.mult_sing(current))
            product = product.add(p.mult_sing(current))
            current = current.next

        return product

    # create a string representation of the polynomial
    def __str__(self):
        count = 0
        current = self.first
        list = ''
        while (current != None):
            if current.coeff != 0:
                list = list + '(' + str(current.coeff) + ', ' + str(current.exp) + ') + '
            current = current.next

        return list[:-3]


def main():
    # read data from file poly.in from stdin
    p = LinkedList()
    q = LinkedList()

    len1 = sys.stdin.readline()
    for i in range(int(len1)):
        current = sys.stdin.readline()
        list = current.split()
        p.insert_in_order(int(list[0]), int(list[1]))

    # accounts for blank line between the two sets of numbers
    sys.stdin.readline()

    len2 = sys.stdin.readline()
    for i in range(int(len2)):
        current = sys.stdin.readline()
        list = current.split()
        q.insert_in_order(int(list[0]), int(list[1]))

    # create polynomial p

    # create polynomial q

    # get sum of p and q and print sum
    print(p.add(q))
    # get product of p and q and print product
    print(p.mult(q))


if __name__ == "__main__":
    main()
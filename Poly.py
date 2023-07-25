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

    # insert at the beginning of a list
    def beginning(self, coeff, exp):
        link = Link(coeff, exp)
        link.next = self.first
        self.first = link

    # insert at end of list
    def end(self, coeff, exp):
        link = Link(coeff, exp)
        current = self.first
        if current is None:
            self.first = link
        while current.next is not None:
            current = current.next
        current.next = link

        # finds exponent in list

    def exp_in_list(self, exp):
        current = self.first
        if current is None:
            return None

        while current.exp != exp:
            if current.next is None:
                return None
            else:
                current = current.next

    def length(self):
        length = 0
        current = self.first
        while current.next is not None:
            length += 1
            current = current.next

        return length

    # keep links in descending order of exponents
    def insert_in_order(self, coeff, exp):

        link = Link(coeff, exp)
        current = self.first
        if current is None:
            self.first = link
            return
        for i in range(self.length() + 1):
            if current.exp <= exp:
                break
            prev = current
            current = current.next
        if current == self.first:
            self.beginning(coeff, exp)
        elif current is None:  # end of list
            self.end(coeff, exp)
        else:
            link.next = prev.next
            prev.next = link

    # code to delete a link

    def delete(self, exp):
        prev = self.first
        current = self.first
        if current is None:
            return None
        while current.exp != exp:
            if current.next is None:
                return None
            else:
                prev = current
                current = current.next

        if current is self.first:
            self.first = current.next
        else:
            prev.next = current.next
        return current.exp

    # add polynomial p to this polynomial and return the sum
    def add(self, p):
        current = self.first
        total = LinkedList()
        while (current is not None):
            prev = total.exp_in_list(current.exp)
            if prev is None:
                total.insert_in_order(current.coeff, current.exp)
            else:
                total.delete(current.exp)
                total.insert_in_order(int(current.coeff) + int(prev), current.exp)
            current = current.next

        current = p.first
        while current is not None:
            prev = total.exp_in_list(current.exp)
            if prev == None:
                total.insert_in_order(current.coeff, current.exp)
            else:
                total.delete(current.exp)
                total.insert_in_order(int(current.coeff) + int(prev), current.exp)
            current = current.next

        return total

    # distribute one of the terms of self to p
    def mult_helper(self, term):
        product = LinkedList()
        current = self.first

        # multiply coefficients and add exponents
        while current is not None:
            link = Link(int(current.coeff) * int(term.coeff), current.exp + term.exp)
            product.insert_in_order(link.coeff, link.exp)
            current = current.next
        return product

    # multiply polynomial p to this polynomial and return the product
    def mult(self, p):
        prod = LinkedList()
        current = self.first
        while current is not None:
            prod = prod.add(p.mult_helper(current))
            current = current.next
        return prod

    # create a string representation of the polynomial

    def __str__(self):
        current = self.first
        output = ''

        while current is not None:
            if current.coeff != 0:
                output = output + str(current) + ' + '
            current = current.next
        return output[:-3]


def main():
    # read data from poly.in from stdin
    num_terms1 = sys.stdin.readline().strip()
    terms1 = []
    for i in range(int(num_terms1)):
        list1 = sys.stdin.readline().strip().split()
        terms1.append(list1)

    sys.stdin.readline()

    num_terms2 = sys.stdin.readline()
    terms2 = []
    for i in range(int(num_terms2)):
        list2 = sys.stdin.readline().strip().split()
        terms2.append(list2)

    # create polynomial p
    poly_p = LinkedList()
    for j in range(int(num_terms1)):
        current = Link(int(terms1[j][0]), int(terms1[j][1]))
        poly_p.insert_in_order(current.coeff, current.exp)

    # create polynomial q

    poly_q = LinkedList()
    for j in range(int(num_terms2)):
        current = Link(int(terms2[j][0]), int(terms2[j][1]))
        poly_q.insert_in_order(current.coeff, current.exp)

    # get sum of p and q and print sum
    sum_linked = poly_p.add(poly_q)
    print(sum_linked)

    # get product of p and q and print product
    prod_linked = poly_p.mult(poly_q)
    print(prod_linked)

    # print(poly_p)
    # print(poly_q)


if __name__ == '__main__':
    main()

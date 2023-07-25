# File: CongoLine.py
# Description: Conduct pair-wise swaps in a linked list
# Student Name: Dharsan Selvakumar
# Student UT EID: ss96967
# Course Name: CS 313E
# Unique Number: 52535


import sys


# DO NOT EDIT THE LINK CLASS DEFINITION BELOW
class Link(object):
    def __init__(self, name="UNNAMED", next=None):
        self._name = name  # _name is private - don't access or modify
        self.next = next

    def __str__(self):
        return self._name


# Input: the head Link of a linked list
# Output: returns the new head of the linked list after swapping

def swap(head, len_list):
    if len_list == 0:
        return None
    if len_list % 2 == 0:
        if head.next is None:
            return head
        elif





# ------- BE CAREFUL EDITING ANTYING BELOW THIS LINE --------
# Input: head of linked list
# Output: prints linked list to stdout
def printList(head):
    if (not head):
        print("__END__")
        return
    print(str(head))
    printList(head.next)


def main():
    # read input
    input = sys.stdin.readlines()
    # build linked list
    next = None
    len_list = input[0]
    for str in reversed(input[1::]):  # ignores length
        next = Link(str.strip(), next)
    # conduct swaps and print results
    printList(swap(next, len_list))


if __name__ == "__main__":
    main()

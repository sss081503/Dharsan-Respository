#  File: Radix.py

#  Description:

#  Student Name:

#  Student UT EID:

#  Partner Name:

#  Partner UT EID:  a

#  Course Name: CS 313E

#  Unique Number:

#  Date Created:

#  Date Last Modified:

import sys


class Queue(object):
    def __init__(self):
        self.queue = []

    # add an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # remove an item from the beginning of the queue
    def dequeue(self):
        return (self.queue.pop(0))

    # check if the queue if empty
    def is_empty(self):
        return (len(self.queue) == 0)

    # return the size of the queue
    def size(self):
        return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort(a):
    queues = [Queue() for i in range(37)] # make list of queues
    # 10 numbers + 26 letters + 1 final queue = 37

    # put all the terms of a into the final queue
    for term in a:
        queues[36].enqueue(term)

    #find max length of a term
    num_passes = 0
    max_length = len(a[0])
    for i in range(len(a)):
        if len(a[i]) > max_length:
            max_length = len(a[i])
    num_passes += max_length

    # making all terms the same length by adding !
    for i in range(len(a)):
        val = a[i]
        if num_passes >= len(val):
            diff = num_passes - len(val)
            for k in range(diff):
                val = val + '!'

    for i in range(1, num_passes + 1): # pass through it num_passes times
        for j in range(queues[36].size()): # for each term in the final queue
            term = queues[36].dequeue()
        #some terms will not be long enough, so we can assume they have 0's at the end



    # remove !


    return


def radix_sort(a):
    # initiate list of 36 queues for radix sort
    queues = [Queue() for i in range(37)]

    # loop through the final queue and enqueue all items in a
    for item in a:
        queues[36].enqueue(item)

    # pass n times
    # where n is equal to the length of the longest string
    n = len(max(a, key=len))
    for p in range(1, n + 1):
        # for each item in the final queue

        for i in range(queues[36].size()):
            # dequeue the item
            item = queues[36].dequeue()

            # calculate its corresponding queue index
            # we assume shorter strings have trailing zeros
            if n - p >= len(item):
                # set the current character to be a 0 if
                # the current string is too short for this pass
                char = 0
            else:
                # otherwise get the character for this pass
                char = item[n - p]
                # if it is a number
                if char.isnumeric():
                    # convert to int
                    char = int(char)
                # if it is a letter
                else:
                    # map it to an int that corresponds with
                    # a queue index
                    char = ord(char) - 87

            # queue this item based on
            # the character examined in this pass
            queues[char].enqueue(item)

        # after the pass is over loop through all queues
        for queue in queues:
            for i in range(queue.size()):
                # dequeue them from their current queue
                # and enqueue them to the last queue
                queues[36].enqueue(queue.dequeue())

    # initialize result list
    res = []
    # loop through the final queue and dequeue all items
    for i in range(queues[36].size()):
        # then append to result
        res.append(queues[36].dequeue())

    # return the result
    return res


def main():
    # read the number of words in file
    line = sys.stdin.readline()
    line = line.strip()
    num_words = int(line)

    # create a word list
    word_list = []
    for i in range(num_words):
        line = sys.stdin.readline()
        word = line.strip()
        word_list.append(word)

    '''
    # print word_list
    print (word_list)
    '''

    # use radix sort to sort the word_list
    sorted_list = radix_sort(word_list)

    # print the sorted_list
    print(sorted_list)


if __name__ == "__main__":
    main()


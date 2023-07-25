#  File: Boxes.py

#  Description:

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name: Alexandar Pinnarwan

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/17/2022

#  Date Last Modified: 10/18/2022

import sys


# Input: 2-D list of boxes. Each box of three dimensions is sorted
#        box_list is sorted
# Output: function returns two numbers, the maximum number of boxes
#         that fit inside each other and the number of such nesting
#         sets of boxes
def nesting_boxes(box_list):

    # creating 2 lists, one for max boxes that fit inside and one for the different sets

    boxes = [0 for x in box_list]
    sets = [0 for x in box_list]

    #to find the max number of boxes that fit inside each other
    for i in range(0, len(box_list)):
        j = i - 1
        max_val = 0

        while j >= 0:
            if does_fit(box_list[j], box_list[i]):
                count = boxes[j]
                if count >= max_val:
                    max_val = count
            j = j - 1

    # to find the different sets of boxes
        j = i - 1

        while j >= 0:

            val1 = max_val

            if does_fit(box_list[j], box_list[i]):
                if boxes[j] == val1:
                    sets[i] += sets[j]

            j = j - 1
        boxes[i] = max_val + 1

        if sets[i] == 0:
            sets[i] = 1

    maximum = max(boxes)
    num_sets = 0

    for q in range(len(sets)):

        if boxes[q] == maximum:
            num_sets = num_sets + sets[q]

    return maximum, num_sets


# returns True if box1 fits inside box2
def does_fit(box1, box2):
    return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])


def main():
    # read the number of boxes
    line = sys.stdin.readline()
    line = line.strip()
    num_boxes = int(line)

    # create an empty list for the boxes
    box_list = []

    # read the boxes from the file
    for i in range(num_boxes):
        line = sys.stdin.readline()
        line = line.strip()
        box = line.split()
        for j in range(len(box)):
            box[j] = int(box[j])
        box.sort()
        box_list.append(box)

    # print to make sure that the input was read in correctly
    # print (box_list)
    print()

    # sort the box list
    box_list.sort()

    # print the box_list to see if it has been sorted.
    # print (box_list)
    print()

    # get the maximum number of nesting boxes and the
    # number of sets that have that maximum number of boxes
    max_boxes, num_sets = nesting_boxes(box_list)

    # print the largest number of boxes that fit
    print(max_boxes)

    # print the number of sets of such boxes
    print(num_sets)


if __name__ == "__main__":
    main()

#  File: Palindrome.py

#  Description:

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/02/2022

#  Date Last Modified: 10/03/2022

# Input: a lowercase string with no digits, punctuation marks, or spaces
# Output: a string that is the smallest palindrome that can be
#         made by adding characters to the start of the input string
import sys

def smallest_palindrome(str):
    if len(str) == 1:
        return str

    if len(str) == 2:
        if str[0] == str[1]:
            return str
        else:
            new_str = str[1] + str
            return new_str
    char_list = []

    i = len(str) - 1
    while i in range(len(str) - 1, 0, -1):
        if str[i] != str[0]:
            char_list.append(str[i])
            i = i-1
        else:
            check = str[i]
            count = 0
            k = i-1
            while k in range(i - 1, 0, -1):
                check = check + str[k]
                diff = i - k + 1
                if check != str[0: diff]:
                    for q in range(len(check)):
                        char_list.append(check[q])
                    for r in range(diff):
                        i = i - 1
                        k = k - k
                    break
                else:
                    count = count + 1
                    k = k - 1
            if count == i:
                i = 0


    new_str = ''
    for i in range(len(char_list)):
        new_str = new_str + char_list[i]
    new_str = new_str + str
    return new_str


# Input: no input
# Output: a string denoting all test cases have passed
def test_cases():
    # write your own test cases

    return "all test cases passed"


def main():
    # run your test cases
    '''
    print (test_cases())
    '''

    # read the data
    lines = sys.stdin.readlines()

    # print the smallest palindromic string that can be made for each input
    for i in range(len(lines)):
        palindrome = lines[i].strip()
        print(smallest_palindrome(palindrome))


if __name__ == "__main__":
    main()

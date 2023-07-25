# File: Sort.py  
# Description: Sort a string by occurrences of the characters.

# Student Name: Dharsan Selvakumar
# Student UT EID: ss96967
# Course Name: CS 313E
# Unique Number: 52535

# Input: any valid string
# Output: a string s in descending order based on the number of occurrences of the characters. Break ties of the same value by letting the character with the greater ASCII value come first 
import sys


def frequencySort(s):
    # TODO: Implement me!
    dict_chars = {}
    for i in range(len(s)):
        if s[i] in dict_chars.keys() == False:
            dict_chars[s[i]] = 1
        elif s[i] in dict_chars.keys() == True:
            count = dict_chars[s[i]]
            count = count + 1
            dict_chars[s[i]] = count


'''
    reversed_dict = {}
    for key in dict_chars:
        val = dict_chars[key]
        if val in reversed_dict.keys():
            original_key = reversed_dict[val]
            for i in range(len(original_key)):
                new_key = ''
                if origianl_key[i] > key:
                    new_key = new_key + i
                else:
                    new_key = new_key + key
                    key = ''
        else:
            reversed_dict[val] = key

    sorted_keys = []
    for i in sorted(reversed_dict.keys()):
        sorted_keys.append(i)

    output = ''
    for key in sorted_keys:
        output = reversed_dict[key] + output
    return output
'''
print(frequencySort('tree'))






'''
def main():
    # read the input file from stdin
    string = sys.stdin.readline().strip()
    while (string != ''):
        print(frequencySort(string))
        string = sys.stdin.readline().strip()


# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()

'''

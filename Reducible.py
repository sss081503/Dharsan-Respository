#  File: Reducible.py

#  Description:

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 10/20/22

#  Date Last Modified:


import sys


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while (div < limit):
        if (n % div == 0):
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):
    hash_idx = 0
    for i in range(len(s)):
        char = ord(s[i]) - 96  # finding the letter

        hash_idx = const - (hash_idx * 26 + char) % const
    return hash_idx


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    # want to find initial state after hashing
    initial = hash_word(s, len(hash_table))

    if hash_table[initial % len(hash_table)] != '':
        step = step_size(s, 11)
        bool = False
        while bool == False:
            initial = initial + step
            if hash_table[initial % len(hash_table)] == '':  # after a spot is empty
                bool = True
                hash_table[initial % len(hash_table)] = s
    else:  # if that spot is empty
        hash_table[initial % len(hash_table)] = s
    return hash_table



# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    initial = hash_word(s, len(hash_table))
    if (hash_table[initial] == s):
        return True
    else:
        position = step_size(s, 11)
        step = 0
        index = (initial + step * position) % len(hash_table)
        if hash_table[index] == s:
            return True
        else:
            while hash_table[index] != s or index >= len(hash_table):
                step += 1
                index = (initial + step * position) % len(hash_table)
                if index >= len(hash_table):
                    return False

                if hash_table[index] == "":
                    return False
            return True


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    list_chars = list(s)
    if ('a' not in list_chars) and ('i' not in list_chars) and ('o' not in list_chars):
        return False
    if find_word(s, hash_memo):
        return True
    if len(s) == 1:  # if word is one letter, return True if one letter words
        return s == "a" or s == "i" or s == "o"
    elif find_word(s, hash_memo):
        return True
    elif find_word(s, hash_table):
        range = 0
        while range < len(s):
            word = s[:range] + s[range + 1:]
            range = range + 1
            if is_reducible(word, hash_table, hash_memo):
                insert_word(s, hash_memo)
                return True
    return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
    longest_words = []
    if len(string_list) >= 1:
        max_length = len(string_list[0])
        longest_words.append(string_list[0])
        for i in range(1, len(string_list)):
            if len(string_list[i]) == max_length:
                longest_words.append(string_list[i])
            elif len(string_list[i]) > max_length:
                longest_words = [string_list[i]]
                max_length = len(string_list[i])
    return longest_words


def main():
    # create an empty word_list
    word_list = []
    # read words from words.txt and append to word_list
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)

    # find length of word_list
    len_list = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    prime = 2 * len_list + 1
    while (is_prime(prime) == False):
        prime = prime + 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for i in range(prime):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for i in word_list:
        insert_word(i, hash_list)

    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    hash_memo = []

    # populate the hash_memo with M blank strings
    m = int(0.2 * len_list) + 1
    # m = 2 * len_list + 1
    while is_prime(m) == False:
        m = m + 1
    for i in range(m):
        hash_memo.append('')

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for p in word_list:
        if is_reducible(p, hash_list, hash_memo):
            reducible_words.append(p)

    # find the largest reducible words in reducible_words
    biggest_words = []
    if len(reducible_words) != 0:
        biggest_words = get_longest_words(reducible_words)

    # print the reducible words in alphabetical order
    # one word per line
    biggest_words.sort()

    if len(biggest_words) != 0:
        for h in biggest_words:
            print(h)


if __name__ == "__main__":
    main()

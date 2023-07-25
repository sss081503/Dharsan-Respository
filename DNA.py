#  File: DNA.py

#  Description: A0

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52535

#  Date Created: 8/26/22

#  Date Last Modified: 8/29/22

# Input: s1 and s2 are two strings that represent strands of DNA
# Output: returns a sorted list of substrings that are the longest
#         common subsequence. The list is empty if there are no
#         common subsequences.
import sys


def all_substrings(s):
    result = []
    # define size of window
    wnd = len(s)

    # generate all substrings
    while wnd > 0:
        idx = 0
        while (idx + wnd) <= len(s):
            sub_str = s[idx:idx+wnd]
            result.append(sub_str)
            idx += 1

            # decrease the size of the window
        wnd -= 1

    # return the result
    return result


def longest_subsequence(s1, s2):
    if len(s1) <= len(s2):
        smaller_string = s1
        larger_string = s2
    else:
        smaller_string = s2
        larger_string = s1

    all_DNA_substrings = all_substrings(smaller_string)

    matches = {}
    len_matches = {}

    for i in range(len(all_DNA_substrings)):
        current_substring = all_DNA_substrings[i]
        matches[current_substring] = larger_string.find(current_substring)
        if larger_string.find(current_substring) != -1:
            len_matches[current_substring] = len(current_substring)

    print(len_matches)





    return ''


def test_cases():
    # test the function longest_subsequence
    assert longest_subsequence("a", "a") == ["a"]
    assert longest_subsequence("abcd", "bc") == ["bc"]
    assert longest_subsequence("abcd", "xyz") == []
    assert longest_subsequence("abcdef", "cde") == ["cde"]
    assert longest_subsequence("hdbdk", "ppppp") == []

    # test the function all_substrings
    assert all_substrings("a") == ["a"]
    assert all_substrings("abc") == ["abc", "ab", "bc", "a", "b", "c"]

    # other test cases

    # return the result
    return "all test cases passed"


def main():
    # call test_cases()

    # read the data
    # read the number of pairs
    num_pairs = sys.stdin.readline()
    num_pairs = num_pairs.strip()
    num_pairs = int(num_pairs)

    print(num_pairs)

    # for each pair find the longest sequence
    for i in range(num_pairs):
        st1 = sys.stdin.readline()
        st2 = sys.stdin.readline()
        # remove end of line character
        st1 = st1.strip()
        st2 = st2.strip()
        # make uppercase
        st1 = st1.upper()
        st2 = st2.upper()
        # print code to check
        print(st1)
        print(st2)
        # get the longest subsequences
        long_sub = longest_subsequence(st1, st2)
        # print the results
        print(long_sub)

    # for each pair
    # call longest_subsequence

    # write out result(s)


# insert blank line

if __name__ == "__main__":
    main()

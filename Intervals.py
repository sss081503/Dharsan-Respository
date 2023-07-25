import sys

#  File: Intervals.py

#  Student Name: Dharsan Selvakumar

#  Student UT EID: ss96967

#  Partner Name: Alexander Pinnarwan

#  Partner UT EID: acp3576

#  Course Name: CS 313E

#  Unique Number: 52535

#  Partner Unique Number: 52530

#  Date Created: 9/8/22

#  Date Last Modified: 9/9/22





# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the
#         interval
def merge_tuples(tuples_list):
        tuples_list.sort()
        i = 0
        while(i + 1 <= len(tuples_list) - 1):
            tuple1 = tuples_list[i]
            tuple2 = tuples_list[i+1]
            if (tuple2[1] < tuple1[0]):
                    i += 1
            elif (tuple2[0] > tuple1[1]):
                    i += 1
            elif (tuple2[0] >= tuple1[0]) and (tuple2[1] <= tuple1[1]):
                    tuples_list[i+1] = tuple1
                    tuples_list.remove(tuple1)
                    i += 0
            elif (tuple2[0] <= tuple1[0]) and (tuple2[1] >= tuple1[1]):
                    tuples_list[i+1] = tuple2
                    tuples_list.remove(tuple1)
                    i += 0
            elif (tuple2[0] >= tuple1[0]) and (tuple2[1] >= tuple1[1]) and (tuple2[0] <= tuple1[1]):
                    new_tuple = (tuple1[0], tuple2[1])
                    tuples_list[i+1] = new_tuple
                    tuples_list.remove(tuple1)
                    i += 0
            elif (tuple2[0] <= tuple1[0]) and (tuple2[1] <= tuple1[1]) and (tuple2[1] >= tuple1[0]):
                    new_tuple = (tuple2[0], tuple1[1])
                    tuples_list[i+1] = new_tuple
                    tuples_list.remove(tuple1)
                    i += 0
        return tuples_list
        

# Input: tuples_list is a list of tuples denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
    tuples_sort = {}
    new_list = []
    for i in range(len(tuples_list)):
        tuple1 = tuples_list[i]
        size = abs(tuple1[1] - tuple1[0])
        if size in tuples_sort:
            previous_tuple = tuples_sort[size]
            if previous_tuple[0] < tuple1[0]:
                tuples_sort[size] = previous_tuple
                key = size + (tuple1[0]/50)
                tuples_sort[key] = tuple1
            elif tuple1[0] < previous_tuple[0]:
                tuples_sort[size] = tuple1
                key = size + (previous_tuple[0]/50)
                tuples_sort[key] = previous_tuple    
        else:
            tuples_sort[size] = tuple1


            

    for i in sorted(tuples_sort.keys()):
        new_list.append(tuples_sort[i])
    return new_list
        
        
# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases
  assert merge_tuples([(1, 4), (-5, 0), (-22, 2), (11, 19), (3, 16)]) == [(-22, 19)]

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases
  assert sort_by_interval_size([((6, 9), (-10, 0), (19, 21))]) == [(19, 21), (6, 9), (-10, 0)]
  
  return "all test cases passed"

def main():
  # open file intervals.in and read the data and create a list of tuples
    num_intervals = sys.stdin.readline()
    interval_list = []
    for i in range(int(num_intervals)):
       interval = sys.stdin.readline()
       interval.strip()
       split1 = interval.split()
       low = int(split1[0])
       high = int(split1[1])
       interval1 = tuple([low, high])
       interval_list.append(interval1)

        
  # merge the list of tuples
    merged_tuples = merge_tuples(interval_list)
    
  # sort the list of tuples according to the size of the interval
    sorted_tuples = sort_by_interval_size(merged_tuples)
    
  # run your test cases
  
   #print(test_cases())

  # write the output list of tuples from the two functions
    print(merged_tuples)
    print(sorted_tuples)
    

if __name__ == "__main__":
  main()

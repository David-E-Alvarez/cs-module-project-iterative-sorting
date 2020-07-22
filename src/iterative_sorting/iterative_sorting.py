# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):#not my code from matt mccarleys cs30 lecture
    print("arr: ", arr)
    # loop through n-1 elements
    for i in range(0, len(arr) - 2):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc(lines of code))
        # Your code here
        for j in range(cur_index + 1, len(arr)):
            if(arr[j]<arr[smallest_index]):
                smallest_index = j
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        # TO-DO: swap
      
        # Your code here

    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    #1.) loop through array and ...
    for i in arr:
        for j in range(0, len(arr)-1):
            if(arr[j] > arr[j + 1]):
                ## a.) compare adjacent elements
                ## b.)swap if not in order
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    #i watched a YT video that showed me how I would re-iterate after iterating through
    #array once because I didn't know how to go back. In the video they use a nested loop which
    #i wouldn't have thought of using #link: https://youtu.be/xli_FI7CuzA

    return arr


print(selection_sort([5,2,1,3,6,4]))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr

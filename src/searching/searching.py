# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # base case
    if end >= start:
        mid = (end + start)
        # fetch middle elem of list and returns it if target
        if arr[mid] == target:
            return mid
        # if elem is < mid, search left subarray
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        #else search right subarray
        else:
            return binary_search(arr, target, end, mid + 1)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    pass
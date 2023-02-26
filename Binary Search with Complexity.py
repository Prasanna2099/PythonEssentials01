def binary_search(arr,x,left,right):
    if right >= left:
        mid = left + (right-left)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr,x,left,mid-1)
        else:
            return binary_search(arr,x,mid+1,right)
    else:
        return -1

import timeit
def search_time(arr,x):
    start = timeit.default_timer()
    binary_search(arr,x,0,len(arr)-1)
    end = timeit.default_timer()
    return end - start

import matplotlib.pyplot as plt
def plot_graph():
    plt.plot(n_values,times)
    plt.xlabel('Number of elements(n)')
    plt.ylabel('Time taken(seconds)')
    plt.title('Binary Search Time Complexity')
    plt.show()

arr = [2,3,4,5,6,7]
x = 6
binary_search(arr,x,2,7);
search_time(arr,x);
plot_graph();

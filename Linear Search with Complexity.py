def linear_search(arr,x):
    for i in range(len(arr)):
        if(arr[i] == x):
            return i
        return -1

from time import perf_counter
n_values = [10,100,1000,10000,100000]
time_taken = []
for n in n_values:
    arr = list(range(n))
    x = n - 1
    start_time = perf_counter()
    result = linear_search(arr,x)
    end_time = perf_counter()
    time_taken.append(end_time - start_time)
print(time_taken)

import matplotlib.pyplot as plt
plt.plot(n_values,time_taken)
plt.xlabel("n(number of elements in list)")
plt.ylabel("Time taken(in seconds)")
plt.title("Linear Search TIme Complexity")
plt.show()

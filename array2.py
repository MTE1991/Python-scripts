n = int(input()) # Total number of elements in a list

arr = [] # Empty list (later filled with int numbers)

for i in range(0,n):
    element = int(input())
    arr.append(element)

# Function to get proportion of +ve, -ve and zeros in a list (1d array):
def plusminus(arr):
    
    # Counters:
    pos = 0
    neg = 0
    zeros = 0

    for i in range(0,n):
        if arr[i] > 0: pos += 1
        elif arr[i] < 0: neg += 1
        else: zeros += 1

    return pos/n, neg/n, zeros/n

print(plusminus(arr))
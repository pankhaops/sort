#mergesort
def mergeSort(a):
    if len(a) > 1:
        m = len(a) // 2
        L, R = a[:m], a[m:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                a[k] = L[i]
                i += 1
            else:
                a[k] = R[j]
                j += 1
            k += 1

        a[k:] = L[i:] + R[j:]


a = [12, 11, 13, 5, 6, 7]

print("Given array:", a)
mergeSort(a)
print("Sorted array:", a)

#quicksort
def quickSort(a, l, h):
    if l < h:
        p = a[h]
        i = l

        for j in range(l, h):
            if a[j] <= p:
                a[i], a[j] = a[j], a[i]
                i += 1

        a[i], a[h] = a[h], a[i]

        quickSort(a, l, i-1)
        quickSort(a, i+1, h)


a = [1, -5, 2, 9, 13, -6, 15]
print("Given array:", a)

quickSort(a, 0, len(a)-1)
print("Sorted array:", a)

#bubblesort
def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

a = [-10, 47, 8, 32, 89, 23, 120]
print("Given array:", a)
bubbleSort(a)
print("Sorted array:", a)

#selection/insertion
def selectionSort(a):
    for i in range(len(a)):
        m = i
        for j in range(i+1, len(a)):
            if a[j] < a[m]:
                m = j
        a[i], a[m] = a[m], a[i]

a = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
print("Given array:", a)

selectionSort(a)
print("Sorted array:", a)

def insertionSort(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key

a = [18, 45, 3, 20, -4]
print("Given array:", a)
insertionSort(a)
print("Sorted array:", a)

#radixsort
def counting_sort(a, exp):
    n, out, c = len(a), [0]*len(a), [0]*10

    for x in a: c[x//exp%10] += 1
    for i in range(1,10): c[i] += c[i-1]

    for x in a[::-1]:
        d = x//exp%10
        out[c[d]-1] = x
        c[d] -= 1
    a[:] = out

def radix_sort(a):
    exp = 1
    while max(a)//exp > 0:
        counting_sort(a,exp)
        exp *= 10

a = list(map(int,input("Enter numbers: ").split()))
radix_sort(a)
print("Sorted array:",*a)




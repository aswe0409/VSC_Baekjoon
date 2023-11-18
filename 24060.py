# n, k = map(int, input().split())
# arr = list(map(int, input().split()))


def merge_sort(A, first, last):
    if first < last:
        mid = (first+last) //2
        merge_sort(A, first, mid)
        merge_sort(A, mid+1, last)
        merge(A, first, last)

def merge(A, first,  last):
    mid = (first + last) // 2
    left = first
    right = last
    temp = []
    m = mid + 1

    while first <= mid and m <= last:
        if A[left] <= A[mid]:
            temp.append(A[left])
            left+=1

        else:
            temp.append(A[m])
            m+=1

    while left <= mid:
        temp.append(A[left])
        left +=1

    while  m<= right:
        temp.append(A[m])
        m += 1

    A[first:last+1] = temp

    return A

print(merge_sort([1,57,6,4], 0, 3))
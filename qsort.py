# from time import time


# data
# data = [5, 3, 2, 4, 1]
data = [7, 15, 2, 4, 6, 1, 3, 8, 5, 9, 12, 10, 11, 14, 13]
# data = [5, 2, 1, 8, 4, 7, 6, 3]

# n = 5
n = len(data)

swap_times = 0
compare_times = 0
elapsed_time = 0


# swap
def swap(t, a, b):  # t: list, a, b: swap index
    tmp = t[a]
    t[a] = t[b]
    t[b] = tmp


print("Before Sorting:", f"{data}\n")


pivot_index = 0
left_index, right_index = 0, n-1


def qsort(data, pivot_index, left_index, right_index):

    # print(data, pivot_index, left_index, right_index)
    if left_index >= right_index:
        return

    print(data, pivot_index, left_index, right_index)
    begin = left_index
    end = right_index

    while left_index < right_index:
        while 1:  # find left index
            if data[left_index] > data[pivot_index]:
                break
            left_index += 1
            if left_index == end:
                break

        while 1:  # find right index
            if data[right_index] < data[pivot_index]:
                break
            right_index -= 1
            if right_index == begin:
                break

        if left_index < right_index:  # check
            swap(data, left_index, right_index)
        else:
            print('swap pivot {} and right {}'.format(data[pivot_index], data[right_index]))
            swap(data, pivot_index, right_index)
            pivot_index = right_index
            print('new pivot index {}, data {}'.format(pivot_index, data))
            break

    qsort(data, begin, begin, pivot_index-1)
    qsort(data, pivot_index+1, pivot_index+1, end)


qsort(data, pivot_index, left_index, right_index)


# print(left_index)
# print(right_index)
print(data)


# compare_times -= swap_times  # compare_times not includes swap_times
# elapsed_time = t1-t0


# print("\nAfter Sorting:", data)
# print("Total Swap Times:", swap_times)
# print("Total Compare Times:", compare_times)
# print("Total Elapsed Time: %f sec" % elapsed_time)

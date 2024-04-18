from qsort import qsort
import random

def test_qsort(n):
    data = [i for i in range(n)]
    random.shuffle(data)
    print("Before Sorting:", f"{data}\n")
    qsort(data, 0, 0, n-1)
    test_result = True;
    for i in range(n-1):
        if i != data[i]:
            test_result = False;
            break;
    return test_result


for i in range(1, 10):
    if not test_qsort(100):
        print("Test {} Failed".format(i))
        break
    else :
        print("Test {} Passed".format(i))

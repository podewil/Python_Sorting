numbers = [54,26,93,17,77,31,44,55,20]

#Source - http://btyy.tistory.com/18
#Python 제자리 정렬기법 (선택정렬, 거품정렬)/EOF(End of File)
# 1. Selection Sort
#        최소값/최대값을 찾아서 맨 앞쪽에 있는 값과 교환하면서 정렬하는 방식
#        *Note: 가장 직관적인 방법이나 1000개 미만의 소량의 데이터에 적합하며 데이터가 많아질수록 비효율적

import random

ulist=[x for x in range(1,101)]
random.shuffle(ulist)
print(ulist)

def min_idx(start, lists):
    index=start
    mini=lists[start]
    end=len(lists)

    for i in range(start, end):
        if mini > lists[i]:
            mini = lists[i]
            index = i
            return index

#def selection_sort(lists):
#    end = len(lists)
#    for i in range(end):
#        idx = min_idx(i, lists)
#        if i != idx:
#            lists[i], lists[idx]=lists[idx], lists[i]
#print(selection_sort(ulist))

#( Selection Sort )=================================================================================================
def selection_sort(ulist):

    if ulist !=[]:
        x = min(ulist)                                  # min: ascending order max: descending order
        ulist.remove(x)
        return[x]+selection_sort(ulist)
    else:
        return[]

print("Selection Sorted numbers are:", selection_sort(numbers))
#=======================================================================================================================



""""#( Tail-recursion Sort )============================================================================================
def tail_recursion_sort(ulist, xlist=[]):
    if ulist!=[]:
        x=min(ulist)                                    # min: ascending order max: descending order
        ulist.remove(x)
        xlist += [x]
        return tail_recursion_sort(ulist, xlist)
    else:       #if empty array
        return xlist

print("Tail-recursion sorted numbers are:", tail_recursion_sort(numbers))
#=======================================================================================================================
"""
""""#( Tail-recursion Sort )============================================================================================
def loop_sort(ulist):
    xlist=[]

    while len(ulist)>0:
        x=min(ulist)                                    # min: ascending order max: descending order
        ulist.remove(x)
        xlist.append(x)
    return xlist

print("Loop sorted numbers are:", loop_sort(numbers))
#=======================================================================================================================
"""
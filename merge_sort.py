# Source - http://btyy.tistory.com/19
# 분할-정복 기법 (Divide & Conquer)
#   - 처리하기 어려운 많은 데이터도 작은 단위로 쪼개면 처리가 가능함
#   - 정렬뿐만 아니라 대부분의 문제에 효과적으로 적용 가능
#   - 합병정렬, 퀵정렬, 힙 정렬등이 분할-정복 기법을 기반으로 동작함
#-----------------------------------------------------------------------------------------------------------------------
# Merge Sort (합병정렬)
# 데이터를 하나의 원소 단위로 각각 분할한 다음 인접한 원소끼리 정렬을 하면서 합병해주는 방식
# 분할/정복 기법을 사용하는 대표적 알고리즘
# 재귀적 용법이 이런 문제에서 얼마나 효율적으로 동작할 수 있는지 확인이 가능함
# 아래 코드는 재귀적 용법을 이용해서 합병정렬

def merge(left, right):
    print("left:", left, "right:", right)
    tmp = []
    while left != [] and right != []:
        if left[0] > right[0]:
            tmp = tmp + [right[0]]
            right.remove(right[0])
        else:
            tmp = tmp + [left[0]]
            left.remove(left[0])
    if left != []:
                tmp = tmp + left
    else:
                tmp = tmp + right
    print("merge:", tmp)
    return tmp


def divide(lists):
    size = len(lists)
    mid = size//2

    if size != 1:
        return merge(divide(lists[:mid]), divide(lists[mid:]))
    else:
        return lists

unorder = [7, 5, 8, 3, 1, 2, 4, 0]
divide(unorder)
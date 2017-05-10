
#Source - http://btyy.tistory.com/18
#Python 제자리 정렬기법 (선택정렬, 거품정렬)/EOF(End of File)
# 2. Bubble Sort
#        두 인접한 원소를 비교해서 정렬하는 방법
#        *Note: 선택정렬과 같이 소규모 데이터에 어울리는 정렬 방법
#        최악의 경우 (배열의 길이*배열의 길이) 만큼의 횟수로 동작해야 함

import random
#=======================================================================================================================
ulist=[x for x in range(1,11)]
print("original ulist: ", ulist)

random.shuffle(ulist)
print("random shuffle ulist:", ulist)

for j in range(len(ulist)-1):
    for i in range(len(ulist)-1):
        if ulist[i]>ulist[i+1]:
            ulist[i], ulist[i+1] = ulist[i+1], ulist[i]

print(ulist)

#=======================================================================================================================
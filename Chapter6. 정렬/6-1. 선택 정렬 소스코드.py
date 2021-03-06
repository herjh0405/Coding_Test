# 정렬이란 데이터를 특정한 기준에 따라서 순서대로 나열하는 것을 말한다.
# 프로그램에서 데이터를 가공할 때 대부분 정렬해서 사용하는 경우가 많기에 정렬 알고리즘은
# 프로그램을 작성할 때 가장 많이 사용되는 알고리즘 중 하나다.
# 정렬을 공부하면 '알고리즘의 효율성'을 쉽게 이해할 수 있다.
# 면접에서도 단골 문제로 출제되니 꼭 기억해두자.
# 데이터를 보고 우리의 뇌는 우리도 모르게 데이터의 규칙성을 파악한다
# 하지만 컴퓨터는 인간과 다르게 규칙성을 직관적으로 알 수 없으며, 어떻게 정렬을 수행할지에 대한 과정을 소스코드로 작성하여 구체적으로 명시해야한다.

## 선택정렬
# 데이터가 무작위로 여러 개 있을 때, 이 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그다음 작은 데이터를 선택해
# 앞에서 두 번째 데이터와 바꾸는 과정을 반복하면 어떨까? 이 방법은 가장 원시적인 방법으로 매번 '가장 작은 것을 선택'한다는 의미에서
# 선택 정렬 알고리즘이라 한다.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

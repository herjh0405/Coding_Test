# 퀵 정렬은 지금까지 배운 정렬 알고리즘 중에 가장 많이 사용되는 알고리즘이다.
# 퀵 정렬은 기준을 설정한 다음 큰 수와 작은 수를 교환한 후 리스트를 반으로 나누는 방식으로 동작한다
# 참 들을 때마다 사고 방식이 대단하다고 느낀다.
# 퀵 정렬에서는 피벗(pivot)이 사용된다. 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 '기준'을 피벗이라 한다.
# 퀵 정렬을 수행하기 전에는 피벗을 어떻게 설정할 것인지 미리 명시해야 한다.
# 피벗을 설정하고 리스트를 분할하는 방법에 따라서 여러 가지 방식으로 퀵 정렬은 구분하는데, 이 책에서는
# 가장 대표적인 분할 방식인 호어 분할 방식을 기준으로 설명한다.
# 호어 분할 방식에서는 다음과 같은 규칙에 따라서 피벗을 설정한다.
# * 리스트에서 첫 번째 데이터를 피벗으로 정한다.
# 이와 같이 피벗을 설정한 뒤에는 왼쪽에서부터 피벗보다 큰 데이터를 찾고, 오른쪽에서부터 피벗보다 작은 데이터를 찾아 위치를 교환해준다.
# 이 과정을 반복하면 '피벗'에 대하여 정렬이 수행된다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end) :
    if start >= end : # 원소가 1개인 경우 종료
        return
    pivot = start # 0
    left = start + 1 # 1
    right = end # 9
    while left <= right : # 조건 1
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot] : # 조건2 : 조건 1이 참일 때만
            left += 1 # 조건2-1 : 1과 2 모두 참일 때
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot] : # 조건3 : 조건 1이 참이고, 조건 2의 작업이 끝나고
            right -= 1 # 조건3-1 : 조건 1과 조건 3이 참일 때

        # 조건 1이 참이고, 조건 2와 3의 작업이 끝난 후
        if left > right : # 엇갈렸다면 작은 right -= 1 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else : # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 / 이 부분이 진짜 대박이네
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

# while문이 2개니까 순간 헷갈려서 찍어보면서 이해함
#
quick_sort(array, 0, len(array)-1)
print(array) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


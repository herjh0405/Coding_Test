array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array) :
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1 :
        return array

    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 퀵 정렬의 경우 앞의 정렬들이 시간 복잡도 O(N^2)을 띄는 것에 반해 O(NlonN)이다.
# 하지만 데이터가 무작위로 입력되어 있는 경우가 아닌 정렬되어 있을 경우에는 느리게 작동 함.(O(N^2))
# 삽입정렬과 반대의 성질을 가짐
# 실제로는 최악의 경우에도 시간 복잡도가 O(NlogN)이 될 수 있게 설정되어 있으니 사용할 때는
# 큰 걱정하지 않아도 됨.

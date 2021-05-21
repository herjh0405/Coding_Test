# 이진 탐색은 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
# 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾아냄
# 시간 복잡도가 O(logN)이다.
def binary_search(array, target, start, end):
     if start > end :
          return None
     mid = (start + end) // 2
     # 찾은 경우 중간점 인덱스 반환
     if array[mid] == target :
          return mid
     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
     elif array[mid] > target :
          return binary_search(array, target, start, mid - 1)
     # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
     else :
          return binary_search(array, target, mid+1, end)

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None : 
     print('원소가 존재하지 않습니다.')
else :
     print(result+1)
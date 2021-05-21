def binary_search(array, target, start, end) :
     while start <= end :
          mid = (start+end)//2
          # 찾은 경우 인덱스 반환
          if array[mid] == target :
               return mid
          # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
          elif array[mid] > target :
               end = mid -1
          # 중간점의 값보다 찾고자 하는 값이 큰 경우 왼쪽 확인
          else :
               start = mid + 1
     return None

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

# 이진 탐색은 코딩 테스트에서 단골로 나오는 문제이니 암기를 추천한다
# 처리해야할 데이터의 개수나 값이 1000만 단위 이상으로 넘어가면 이진 탐색과 같은 O(logN)의 속도를 내야하는 알고리즘이 필요하다
# 전형적인 이진 탐색 문제이자, 파라메트릭 서치 유형의 문제이다.
# 파라메트릭 서치는 최적화 문제를 결정 문제로 바꾸어 해결하는 기법이다.
# '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 사용.

# 문제의 풀이는 은근 간단하다. 적절한 높이를 찾을 때까지 절단기의 높이 H를 반복해서 조정한다.
# 현재 이 높이로 자르면 조건을 만족할 수 있는가?를 확인한 뒤에 조건의 만족 여부(Yes or No)에 따라서 탐색 범위를 좁혀서 해결 가능
# 범위를 좁힐 때 이진 탐색의 원리를 사용
# 절단기의 높이는 1부터 10억까지의 정수 중 하나이다. 큰 수를 보면 당연하게 이진 탐색을 떠올려야한다.

import sys
# 떡의 개수(N)과 요청한 떡의 길이(M)을 입력받기
n, m = list(map(int, sys.stdin.readline().split()))
# 각 떡의 개별 높이 정보를 입력받기
array = list(map(int, sys.stdin.readline().split()))

# 이진 탐색을 위한 시작점과 끝점 설정
start = 0
end = max(array)

# 이진 탐색 수행(반복적)
result = 0
while(start <= end) :
     total =0
     mid = (start + end) // 2
     for x in array :
          # 잘랐을 때의 떡의 양 계산
          if x > mid :
               total += x - mid
     # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
     if total < m : 
          end = mid - 1
     # 떡의 양이 충분한 경우 덜 자르기 (오른쪽 부분 탐색)
     else : 
          result = mid # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
          start = mid + 1
     
print(result)
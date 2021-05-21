# 동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
# 어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
# 동빈이를 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를작성해야 한다.
# 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
# Ex)
# 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다.
# N=5, [8, 3, 7, 9, 2]
# 손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.
# M=3, [5, 7, 9]
# 이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력한다. 구분은 공백으로 한다.
import sys
# 이진 탐색 코드 작성
def binary_search(array, target, start, end) :
     while start <= end :
          mid = (start + end) // 2
          if array[mid] == target :
               return mid 
          elif array[mid] > target :
               end = mid -1 
          else : 
               start = mid + 1
     return None
# N 가게의 부품 수 입력
n = int(sys.stdin.readline().rstrip())
# 가게의 부품 번호 입력
array = list(map(int, sys.stdin.readline().split()))
array.sort() # 이진 탐색에 sort
# 손님이 요청한 부품 개수
m = int(sys.stdin.readline().rstrip())
vi_list = list(map(int, sys.stdin.readline().split()))

for vi in vi_list :
     result = binary_search(array, vi, 0, n-1)
     if result == None :
          print('no', end=' ')
     else :
          print('yes', end=' ')

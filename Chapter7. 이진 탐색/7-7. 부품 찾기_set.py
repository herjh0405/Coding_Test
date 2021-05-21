import sys
n = int(input())
array = set(map(int, sys.stdin.readline().split()))

m = int(input())
vi_list = list(map(int, sys.stdin.readline().split()))

for vi in vi_list : 
     if vi in array :
          print('yes', end = ' ')
     else :
          print('no', end = ' ')
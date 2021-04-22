
# 탐색이란 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
# DFS/BFS가 대표적임 -> 이 알고리즘에서는 기본 자료구조인 스택과 큐에 대한 이해가 필요
# 자료구조란 데이터를 표현하고 관리하고 처리하기 위한 구조를 의미함.
# Stack : FILO
stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력 / list[A:B:C] : A부터 B까지 C의 간격으로, None이면 처음부터 할 수 있는데까지 한칸씩, C가 음수이면 역순


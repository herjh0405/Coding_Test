# 최단 경로 알고리즘은 말 그대로 가장 짧은 경로를 찾는 알고리즘이다.
# 길 찾기 문제라고도 불리며, 다양한 종류의 유형이 있는데, 상황에 맞는 효율적인 알고리즘이
# 정립되어 있다. 학부 수준에서는 다익스트라, 플로이드 워셜, 벨만 포드 알고리즘 3가지가 있다.
# 이 책에서는 그 중 가장 많이 등장하는 다익스트라와 플로이드 워셜 알고리즘을 다룬다.

# 다익스트라 최단 경로 알고리즘은 그래프에서 여러 개의 노드가 있을 때, 특정한 노드에서 출발하여
# 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘 (음의 간선이 없을 때 정상적으로 작동 -> GPS 기본 알고리즘)
# 1. 출발 노드를 설정한다.
# 2. 최단 거리 테이블을 초기화한다.
# 3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블을 갱신한다.
# 5. 위 과정에서 3과 4번을 반복한다.

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int, input().split())
# 시작 노드의 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]
# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False]*(n+1)
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m) :
     a, b, c = map(int, input().split())
     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
     graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node() :
     min_value = INF
     index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
     for i in range(1, n+1) :
          if distance[i] < min_value and not visited[i] :
               min_value = distance[i]
               index = i
     return index

def dijkstra(start):
     # 시작 노드에 대해서 초기화
     distance[start] = 0
     visited[start] = True
     for j in graph[start] :
          distance[j[0]] = j[1]
     # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
     for i in range(n-1) :
          # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
          now = get_smallest_node()
          visited[now] = True
          for j in graph[now] :
               cost = distance[now] + j[1]
               if cost < distance[j[0]] :
                    distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1) :
     # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
     if distance[i] == INF :
          print('INFINITY')
     # 도달할 수 있는 경우 거리를 출력
     else:
          print(distance[i])












# N명의 학생 정보가 있다. 학생 정보는 학생의 이름과 학생의 성적으로 구분된다.
# 각 학생의 이름과 성적 정보가 주어졌을 때 성적이 낮은 순서대로 학생의 이름을 출력하는 프로그램을 작성하시오.

n = int(input()) # 2
ans_list = [[] for _ in range(n)]
for i in range(n) :
    input_data = input().split() # 홍길동 95 이순신 77
    ans_list[i] = input_data[0], int(input_data[1])

ans_list = sorted(ans_list, key=lambda x : x[1])

for student in ans_list :
    print(student[0], end = ' ') # 이순신 홍길동

# 이 문제에서는 학생의 정보가 최대 100,100개까지 입력될 수 있으므로
# 최악의 경우 O(NlogN)을 보장하거나 O(N)을 보장하는 계수 정렬을 사용하면 된다.
# 그뿐 아니라 입력되는 데이터는 학생의 이름과 점수지만 출력할 때는 학생의 이름만
# 출력하면 되므로 학생 정보를 (점수, 이름)으로 묶은 뒤에 점수를 기준으로 정렬을 수행해야 한다.
# 이 경우에도 마찬가지로 파이썬의 기본 정렬 라이브러리를 사용하는 것이 효과적이다.
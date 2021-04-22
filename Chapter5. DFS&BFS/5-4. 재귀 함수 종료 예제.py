# 재귀 함수는 종료 조건을 꼭 명시해야 한다. 잘못하면 무한 호출될 수 있기 때문
def recursive_function(i):
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100 :
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료합니다.')

recursive_function(1)

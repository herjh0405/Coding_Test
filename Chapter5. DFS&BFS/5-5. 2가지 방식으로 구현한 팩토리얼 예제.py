# 컴퓨터 내부에서 재귀 함수의 수행은 스택 자료구조를 이용한다.
# 함수를 계속 호출했을 떄 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문이다.
# 재귀 함수는 내부적으로 스택 자료구조와 동일하다는 것을 기억하자.

# 반복적으로 구현한 n!
def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1 : # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n*(n-1)!인 코드를 그대로 작성
    return n * factorial_recursive(n-1)

print('반복적으로 구현:', factorial_iterative(5)) # 반복적으로 구현: 120
print('재귀적으로 구현:', factorial_recursive(5)) # 재귀적으로 구현: 120

# 재귀 함수의 장점은 ? 더 간결하다. 수학의 점화식을 그대로 소스코드로 옮겼기 때문
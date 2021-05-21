# 입력 데이터가 많은 문제는 sys 라이브러리의 readline() 함수를 이용하면 시간 초과를 피할 수 있다
import sys
# 하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip() # readline사용시 rstrip사용 필수적, 입력 엔터를 줄 바꿈 기호로 인식하는 데 그것을 방지해줌

# 입력받은 문자열 그대로 출력
print(input_data)
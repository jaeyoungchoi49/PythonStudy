# 사용자가 입력한 값이 짝수인지 홀수인지 계산해서 결과를 알려주는 프로그램을 의사코드로 작
# 성하면 다음과 같다.
# 1. 사용자로부터 정수를 입력받는다.
# 2. 입력한 수를 2로 나눠서 나머지 값을 구한다.
# 3. 나머지 값이 1이면 홀수, 0이면 짝수로 분류한다.
# 4. 분류한 결괏값을 출력한다.

i = int(input('숫자를 입력하시오: '))  # int(): 적힌 숫자를 정수로 만듦
if i % 2 == 0:                      # % : 두 수를 나누었을 때의 나머지 값,   == : 같다
    print(str(i) + "는 짝수")        # str(): 숫자를 문자열로 만듦
else:
    print(str(i) + "는 홀수")

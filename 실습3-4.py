# 문자열을 정수로 변환한 후 연산하기
# [실습3-3]에 이어서 이 실습을 한다.
# 변수 number의 자료형을 정수로 변경한다.
# 변수 number에 11을 더한 후 결과를 변수 total에 할당한다.
# 변수 total을 출력한다.

number = input('1과 10 사이의 아무 숫자를 입력하세요[1~10]: ')
print(number)
int(number)
total = int(number) + 11
print(total)
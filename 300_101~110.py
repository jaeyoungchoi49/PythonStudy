# 101
#
# 파이썬에서 True 혹은 False를 갖는 데이터 타입은 무엇인가?
#
# 정답확인
'''bool'''
#
# 102
#
# 아래 코드의 출력 결과를 예상하라
#
# print(3 == 5)
#
# 정답확인
print(3 == 5)
'''False'''
#
# 103
#
# 아래 코드의 출력 결과를 예상하라
#
# print(3 < 5)
#
# 정답확인
print(3 < 5)
'''True'''
#
# 104
#
# 아래 코드의 결과를 예상하라.
#
# x = 4
# print(1 < x < 5)
#
# 정답확인
x = 4
print(1 < x < 5)
'''True'''
#
# 105
#
# 아래 코드의 결과를 예상하라.
#
# print ((3 == 3) and (4 != 3))
#
# 정답확인
print ((3 == 3) and (4 != 3))
'''True'''
# 106
#
# 아래 코드에서 에러가 발생하는 원인에 대해 설명하라.
#
# print(3 => 4)
#
# 정답확인
# print(3 => 4)
'''문장기호를 잘못 적었다.
지원하지 않는 연산자이다.'''
#
# 107
#
# 아래 코드의 출력 결과를 예상하라
#
# if 4 < 3:
#     print("Hello World")
#
# 정답확인
if 4 < 3:
    print("Hello World")
'''조건을 만족하지 않으므로 아무 것도 나오지 않는다'''
#
# 108
#
# 아래 코드의 출력 결과를 예상하라
#
# if 4 < 3:
#     print("Hello World.")
# else:
#     print("Hi, there.")
#
# 정답확인
if 4 < 3:
    print("Hello World.")
else:
    print("Hi, there.")
'''조건을 만족하지 않으므로 else 값이 나온다'''
#
# 109
#
# 아래 코드의 출력 결과를 예상하라
#
# if True :
#     print ("1")
#     print ("2")
# else :
#     print("3")
# print("4")
#
# 정답확인
if True :
    print ("1")
    print ("2")
else :
    print("3")
print("4")
'''아무 조건도 없으므로 
1
2
4'''
#
# 110
#
# 아래 코드의 출력 결과를 예상하라
#
# if True :
#     if False:
#         print("1")
#         print("2")
#     else:
#         print("3")
# else :
#     print("4")
# print("5")
#
# 정답확인
if True :
    if False:
        print("1")
        print("2")
    else:
        print("3")
else :
    print("4")
print("5")
'''아무 조건도 없으므로 
3
5'''
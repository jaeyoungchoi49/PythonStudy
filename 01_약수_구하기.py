# 약수 구하기
# 문제
# 어떤 자연수 p와 q가 있을 때, 만일 p를 q로 나누었을 때
# 나머지가 0이면 q는 p의 약수이다.
# 6을 예로 들면

#     6 ÷ 1 = 6 … 0
#     6 ÷ 2 = 3 … 0
#     6 ÷ 3 = 2 … 0
#     6 ÷ 4 = 1 … 2
#     6 ÷ 5 = 1 … 1
#     6 ÷ 6 = 1 … 0

# 그래서 6의 약수는 1, 2, 3, 6, 총 네 개이다.
#
# 두 개의 자연수 N과 K가 주어졌을 때,
# N의 약수들 중 K번째로 작은 수를 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N과 K가 빈칸을 사이에 두고 주어진다.
# N은 1 이상 10,000 이하이다. K는 1 이상 N 이하이다.
#
# 출력
# 첫째 줄에 N의 약수들 중 K번째로 작은 수를 출력한다.
# 만일 N의 약수의 개수가 K개보다 적어서
# K번째 약수가 존재하지 않을 경우에는 0을 출력하시오.

import random

N = int(input('자연수를 입력하시오: '))
numN =[]
for i in range(1,N+1):
    if N >= 1 and N <= 10000:
        if N % i == 0:
            numN.append(i)

    else:
        print("1 이상 10,000 이하의 자연수를 입력하시오.")
        break
print(numN)

print("약수의 개수: ",len(numN))
K = int(input('원하는 순서의 약수를 입력하시오: '))


if K > len(numN):
    print(0)
else:
    print(numN[K-1])

'''
허정윤 님 풀이

try:
    n, k = map(int, input('숫자를 입력해 주세요').split())
    if not (1 <= n <= 10000 and 1 <= k <= n): # 예외 범위 정하기
        raise Exception('잘못 입력하셨습니다.')
    # a=[i for i in range(1, A+1) if A%i == 0]
    a = []
    for i in range(1, n + 1):
        if n % i == 0:
            a.append(i)

    print(a[k - 1])
except IndexError:
    print(0)
except Exception as e:
    print(e)

# 박혜인 님 풀이

# 약수 구하기

while True:
    N, K = map(int, input().split())
    if 1 <= N <= 10000:
        break

K_list = []     # 약수 저장 리스트

for i in range(1, N+1):
    if N % i == 0:
        K_list.append(i)
    else:
        continue

if len(K_list) < K:
    print('0')
else:
    print(K_list[K-1])

# 박지영 님 풀이

num=input("1<=N<=10,000 1<=K<=N :")
a,b=num.split()

A=int(a)
B=int(b)

yaksu=[i for i in range(1, A+1) if A%i == 0]

print(f'{A}의 약수는 {yaksu} 총{len(yaksu)}개이다.')

if B > len(yaksu):
    print('0')
else:
    print(yaksu[B-1])

'''
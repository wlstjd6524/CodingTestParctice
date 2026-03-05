'''
- solved.ac Class1 - 백준 2231번 문제 (분해합)

- [문제](https://www.acmicpc.net/problem/2231)
'''
# 완전 탐색
n = int(input())

for i in range(1, n+1):
    j = sum(map(int, str(i)))
    if i + j == n:
        print(i)
        break
else:
    print('0')
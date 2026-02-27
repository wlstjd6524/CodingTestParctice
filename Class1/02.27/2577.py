'''
- solved.ac Class1 - 백준 2577번 문제 (숫자의 개수)

- [문제](https://www.acmicpc.net/problem/2577)
'''
a = int(input())
b = int(input())
c = int(input())

t_num = a * b * c

for i in range(10):
    print(str(t_num).count(str(i)))
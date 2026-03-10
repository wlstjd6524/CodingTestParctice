'''
- solved.ac Class1 - 백준 1546번 문제 (평균)

- [문제](https://www.acmicpc.net/problem/1546)
'''
test = int(input())
score = list(map(int, input().split()))
new_sum = 0

max_score = max(score)

for i in score:
    new_sum += i / max_score * 100

print(new_sum / test)
'''
- solved.ac Class1 - 백준 8958번 문제 (OX 퀴즈)

- [문제](https://www.acmicpc.net/problem/8958)
'''
num = int(input())

for i in range(num):
    ox_string = input()
    total_score = 0
    combo = 0

    for j in ox_string:
        if j == 'O':
            combo += 1
            total_score += combo
        else:
            combo = 0
    
    print(total_score)
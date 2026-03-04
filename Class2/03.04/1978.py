'''
- solved.ac Class1 - 백준 1978번 문제 (소수 찾기)

- [문제](https://www.acmicpc.net/problem/1978)
'''
n = int(input())
m = list(map(int, input().split()))
count = 0

for num in m:
    if num == 1:
        continue

    for i in range(2, num):
        if num % i == 0:
            break
    else:
        count += 1

print(count)

'''
새로 알게 된 내용 for, else 구문 
-> else 는 for 문 짝꿍으로도 사용이 가능하다.

로직의 해석은 for 문이 중간에 break 를 만나서 강제로 터지지 않고, 끝까지 무사히 다 돌았을 때만 else 블록이 딱 한번 실행되는 구조
'''
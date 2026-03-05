'''
- solved.ac Class1 - 백준 2292번 문제 (벌집)

- [문제](https://www.acmicpc.net/problem/2292)
'''
# 패턴 : 벌집이 6각형으로 이루어져 있고, 숫자 증감 패턴을 분석해보니까 6의 배수로 마지막 수가 떨어짐
# 2개의 방을 지나가는 경우의 수 : 2 3 4 5 6 7 (총 6개)
# 3개의 방을 지나가는 경우의 수 : 8 9 10 11 12 ... 19 (총12개)
# 4개의 방을 지나가는 경우의 수 : 20 21 22 23 24 ... 37 (총 18개)
# 이런식의 증감패턴을 봤을 때 숫자 n 을 받았을 때 목표숫자에 도달할 때 까지 방수를 count 하면서 계산식을 작성하면 방수 count 를 구할 수 있음
max_num = 1
room_count = 1
n = int(input())

while n > max_num:
    max_num += 6 * room_count
    room_count += 1

print(room_count)
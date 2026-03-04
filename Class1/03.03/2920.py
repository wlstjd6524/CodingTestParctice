'''
- solved.ac Class1 - 백준 2920번 문제 (음계)

- [문제](https://www.acmicpc.net/problem/2920)
'''
# 고민 : 답안지 자체를 리스트로 만들어서 비교할지
# 새로 공부하면서 알게된 sorted() -> 오름차순, 내림차순 확인 가능한 내장함수 를 써볼지
num_list = list(map(int, input().split()))

if num_list == sorted(num_list):
    print('ascending')
elif num_list == sorted(num_list, reverse=True):
    print('descending')
else:
    print('mixed')
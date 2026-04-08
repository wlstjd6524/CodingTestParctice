'''
백준 10818: 최소, 최대
URL : https://www.acmicpc.net/problem/10818
'''
num = int(input())
num_list = list(map(int, input().split()))

num_list.sort()

print(num_list[0], num_list[num - 1])

'''
코드는 성공했지만 아쉬운 점이 발생

문제점1. 일단 리스트 자체를 sort() 하는건 좋지만 이제 속도 측면으로 생각해야 하고, 데이터가 엄청나게 많은 양이 들어온다면 그 데이터들을 하나 씩
        줄 세우는 것은 엄청난 시간이 들 수도 있음
        -> 따라서 이런 문제는 챔피언 변수를 하나 지정해놓고 for 문으로 하나씩 비교하면서 데이터를 비교하는게 더 빠를 수도 있음
        -> 출제자 의도가 완전 탐색으로 풀어보라고 낸 문제일 가능성도 존재한다.
'''

'''
따라서 완전 탐색 접근법으로 풀면 다음과 같이 해결할 수 있겠다

num = int(input())
num_list = list(map(int, input().split()))

# 일단 초기값을 넣어보고 리스트를 처음부터 끝까지 순회하면서 각 값을 비교해서 얘보다 크면 넣는 식으로 하나씩 비교
min_val = num_list[0]
max_val = num_list[0]

for i in range num_list:
    # 최솟값 찾기
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print(min_val, max_val)
'''
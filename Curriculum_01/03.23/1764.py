'''
백준 1764: 듣보잡
URL : https://www.acmicpc.net/problem/1764
'''
N, M = map(int, input().split())
N_set = set()
M_set = set()           # set() 으로 선언, 왜냐면 듣도보도 못한 사람을 찾는거니까 듣지도 보지도 못하는 사람의 set 자료형에 교집합이 존재하면
                        # 그거는 듣도 보도 못한 사람 그리고 그 교집합을 len 으로 출력하면 듣도보도 못한 사람의 수임
                        # 근데 set 도 len() 지원가능? 혹시 모르니까 totla_count 해서 안되면 count 를 올려보자 => 지원가능이면 지워도 됨.
i = 0

'''
while True:
    if i % 2 != 0:      # 이름을 물어보는 로직이 홀수번째는 듣도 못한 사람을 넣고, 짝수번째는 보도 못한 사람을 넣는 구조
        name = input()
        N_set.add(name)
        i += 1
        if i == N:
            break 
    else:
        name = input()
        M_set.add(name)    

compare = (N_set & M_set)

print(len(compare))
print(compare)
'''

# 1. 문제를 잘 못 해석했음 순서가 들어오는건 듣도 못하는 사람 쭈욱 받고, 보도 못하는 사람을 쭈욱 받는 형태였음
# 2. 교집합을 출력하는 건 좋았고 마지막에 출력문에 정렬해서 하나씩 꺼내서 출력하는 형태로 나아가야 함.

for _ in range(N):
    N_set.add(input())      # 이런 형태로 받을 수 있었음

for _ in range(M):
    M_set.add(input())

compare = N_set & M_set

print(len(compare))

for name in sorted(compare):
    print(name)
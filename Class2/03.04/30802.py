'''
- solved.ac Class1 - 백준 30802번 문제 (웰컴 키트)

- [문제](https://www.acmicpc.net/problem/30802)
'''
# 1. 참가자 수 입력
n = int(input())

# 2. 6가지 사이즈별 신청자의 수를 리스트로 입력
sizes = list(map(int, input().split()))

# 3. 티셔츠 묶음 단위(t)와 펜 묶음 단위(p) 입력
t, p = map(int, input().split())

# 4. 티셔츠 최소 묶음 계산
t_bundles = 0
for size in sizes:
    if size == 0:
        continue
        
    t_bundles += size // t        # 일단 몫만큼 묶음을 더함
    if size % t != 0:             # 나머지가 존재한다면 (1명이라도 남는다면)
        t_bundles += 1            # 무조건 1묶음을 추가로 더 사야 함

# 5. 결과 출력
print(t_bundles)                  # 첫째 줄: 티셔츠 총 묶음 수
print(n // p, n % p)              # 둘째 줄: 펜 최대 묶음 수, 남는 펜(낱개) 수
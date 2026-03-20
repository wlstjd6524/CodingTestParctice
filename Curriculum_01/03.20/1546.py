'''
백준 1546: 평균
URL : https://www.acmicpc.net/problem/1546
'''
test_num = int(input())
score = list(map(int, input().split()))
avg = []

max_score = max(score)
min_score = min(score)

for i in range(len(score)):
    avg.append(score[i] / max_score * 100)

print(sum(avg) / test_num)

# 백준 컴파일 완료, 소요시간 : 16분

'''
피드백

1. min_score 와 같이 안쓰는 변수는 제거
2. for 문이 아직도 C언어 다운 for 문임 파이썬 답게 변경이 필요함
    -> for s in score: avg.append(s / max_score * 100)
3. 그리고 해당 문제의 수학적 접근을 조금 더 고민했다면 for 문 자체가 필요 없어질 수 있었음
    -> 지금 보면 값이 바뀌는 부분은 들어오는 모든 점수가 바뀌는 구조임 그니까 나누는 값 이랑 * 100 을 하는건 고정값이기 때문에
    수학적으로 예를 들어 A, B, C 점수가 들어오면 (A + B + C)/M * 100 이랑 같은 구조라는거임

    -> 그래서 이런식으로 코드 다이어트가 가능함
    test_num = int(input())
    score = list(map(int, input().split()))

    print((sum(score) / max_scre * 100) / test_num)
'''
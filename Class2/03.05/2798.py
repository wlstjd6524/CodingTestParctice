'''
- solved.ac Class1 - 백준 2798번 문제 (블랙잭)

- [문제](https://www.acmicpc.net/problem/2798)
'''
n, m = map(int, input().split())
list_n = list(map(int, input().split()))
result = 0

# 3중 for 문으로 카드를 하나씩 뽑아보는데
# for 문으로 들어갈 수록 앞에 뽑은 수의 중복을 없애야 하기 때문에 앞의 for 문의 순회변수에 +1 값을 통해 중복을 피하기
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            current_sum = list_n[i] + list_n[j]  + list_n[k]    # 그래서 하나씩 뽑은 카드를 일단 더해보고 
            if current_sum <= m:                                # 만약에 그 수가 m 이랑 작거나 같으면 (우리 문제의 정답 조건)
                if current_sum > result:                        # 근데 그게 최종 결과로 출력하는 값보다 크면
                    result = current_sum                        # 출력변수에 저장 (이렇게 하면 최대한 가까운 수를 남길 수 있음)

print(result)
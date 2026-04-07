'''
백준 2501: 약수 구하기
URL : https://www.acmicpc.net/problem/2501
'''
n, k = map(int, input().split())
result_list = list()

# 나누기는 1 부터 시작하니까 1 부터 받은 값 까지
# 받은값 이랑 j 로 들어오는 증감하는 숫자가 나머지가 0이면 즉, 나눠 떨어지면 걔는 약수로 판정하고
# 결과로 받을 리스트에 저장 
for i in range(1, n+1):
    if n % i == 0:
        result_list.append(i)

# 그다음 오름차순으로 정렬하고
result_list.sort()

# 만약에 우리가 사용자로 부터 받은 k 개보다 적어서 k번째 약수가 존재하지 않으면 0을 출력
if len(result_list) < k:
    print("0")
# 그런게 아니면 list 의 k번째 약수를 출력 
# k-1 을 하는 이유는 만약 1번째로 작은수를 출력하라고 하면 리스트의 첫 시작은 0번 부터니까 사실상 첫번째로 작은수는 리스트의 0번째
# 값이 정답임 
else:
    print(result_list[k-1])
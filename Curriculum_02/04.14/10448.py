'''
백준 10448: 유레카 이론
URL : https://www.acmicpc.net/problem/10448
'''
# 일단 1000 보다 작은 삼각수를 리스트에 구해놓고
triangel_nums = []
n = 1

while True:
    tn = n * (n+1) // 2     # 삼각수 공식 일단 정의
    if tn > 1000:
        break
    triangel_nums.append(tn)
    n += 1

# 삼각수 리스트를 구해놨으니까 이제 3개 합이 num 이 되는지 확인
def check_eureka(target_num):
    for i in triangel_nums:
        for j in triangel_nums:
            for k in triangel_nums:
                # 3개 합이 우리 타겟 숫자랑 같으면
                if i + j + k == target_num:
                    return 1
                
    # 3중 for 문이 다 돌때까지 정답이 없으면 조합이 없으니까
    return 0

test_case = int(input())
for _ in range(test_case):
    num = int(input())
    # num 을 함수에 넘겨주고 결과값을 받아오기
    print(check_eureka(num))
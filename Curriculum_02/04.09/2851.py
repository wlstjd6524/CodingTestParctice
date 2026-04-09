'''
백준 2851: 슈퍼 마리오
URL : https://www.acmicpc.net/problem/2851
'''
total_num = 0

for _ in range(10):
    num = int(input())

    # 일단 수를 더하고
    total_num += num

    # 여기서 조건문으로 숫자를 갈라야 됨.
    # 조건1. total_num 의 숫자가 딱 100 이면 for 문을 멈추고 total_num 출력
    # 조건2. 수를 더하고 보니까 100 을 넘어버렸어 그러면 방금 num 을 더한게 total_num 이고 total_num 에서 -= num 을 한게 그 전 숫자니까
    # 그 전 숫자랑 지금 더 한 숫자랑 뭐가 더 100 에 가까운지 비교를 해야 됨 (100 - 해당 숫자) 를 했을 때 나온 값이 더 작은 게 100 에 가까운 숫자니까
    # 그 숫자를 출력해야 됨. (근데 100 이 넘어가는 수를 100 - 해당숫자 를 해버리면 음수가 되버려서.. 절대값을 씌워야 할텐데..)

    # 만약에 40 이 쭉 들어오는 수를 가정하면 100 에 가까운 수가 80 이랑 120 이 되버리는데 이 때는 100 이랑 차이가 20 으로 둘 다 똑같은 차이를 가짐
    # 이럴 때는 더 높은 수로 조건문을 덮어버리면 됨.

    
    # 수를 더하고 보니까 100을 넘었거나 100 이면
    if total_num >= 100:
        # 방금 num 을 더하기 전의 숫자
        prev_num = total_num - num

        # 100 이랑 차이를 구해서
        diff_current = abs(100 - total_num)
        diff_prev = abs(100 - prev_num)

        # 차이가 같거나 현재 숫자가 100 에 더 가까우면
        if diff_current <= diff_prev:
            print(total_num)
        else:
            print(prev_num)
        
        # 정답 찾고 종료 
        exit()

# 이 부분은 조건 외 상황임, 버섯 10개를 다 더했는데도 100 이 안넘으면
# 그냥 그 합을 출력해버리면 됨
print(total_num)
'''
백준 2798: 블랙잭
URL : https://www.acmicpc.net/problem/2798
'''
card_count, result_num = map(int, input().split())
card_list = list(map(int, input().split()))

card_list = card_list[::-1]     # 뒤집어
best_sum = 0                         # 최종 출력문

# 로직
# 1. 먼저 뒤집은 list 0 번이 비교하려고 하는 수 보다 작으면 sum += , 크면 애초에 문제 조건에 부합하지 않음
# 2. 다음 인덱스로 넘어가서 다음 인덱스 요소랑 sum 이랑 더했는데, 얘가 비교하는 수 보다 크거나 같으면 이 수는 더하면 안되는 수라서 pass
# 3. 작으면 sum +=
# 4. 여기 까지는 '3번 더해야 하는 조건' 때문에 이런식으로 진행하는데 다음 조건문에는 이미 2번 더해져있는 상태라 크면 버리고 같으면 출력, 작으면 출력

for i in range(card_count):     # 첫 번째 카드를 고르고
    for j in range(i+1, card_count):    # 두 번째 카드도 고름
        for k in range(j+1, card_count):    # 세 번째 카드도 고름
            current_sum = card_list[i] + card_list[j] + card_list[k]

            if current_sum <= result_num and current_sum > best_sum:
                best_sum = current_sum

print(best_sum)
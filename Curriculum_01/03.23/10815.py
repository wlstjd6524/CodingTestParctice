'''
백준 10815: 숫자카드
URL : https://www.acmicpc.net/problem/10815
'''

have_card = int(input())
have_card_num = set(map(int, input().split()))

check_card = int(input())
check_card_num = list(map(int, input().split()))        # 피드백 반영사항 1. 검사할 카드는 List 로

# 처음으로 생각해 본 로직은 compare 이라는 부분에 상근이가 가지고 있는 카드랑, 비교할 카드에 교집합을 하나의 변수에 집어넣음
# 그다음에 비교할 카드랑 교집합을 비교해서 비교할 카드의 i 번째 인덱스가? 교집합이 들어간 변수랑 일치하면 1을 출력하는거고 아니면 0을 출력하는 구조
# 근데 걸리는 부분이 
# 1. if check_card_num[i] == compare: 처럼 선언을 하니 compare 에 접근할 요소가 없어서 접근이 안되고 그렇다고 [i] 처럼 인덱싱을 하자니 무조건
# 범위 에러를 반환할 것 같음
# 2. 두번째는 print("1"), print("0") 식으로 출력하면 붙어서 나오는게 아니라 떨어져서 나올텐데 어떻게 합칠까 고민..
'''
compare = (have_card_num & check_card_num)
for i in range(check_card):
    if check_card_num[i] == compare:
        print("1")
    else:
        print("0")
'''

# 1. 상근이가 가진 카드(have_card_num) 은 이 숫자가 있나 없나? 를 빠르게 찾으면 되서 set 으로, 검사 카드(check_card_num)은 List 로 해야함.
# 2. 교집합 비교 말고 for in 으로 하나씩 검사하되, print 출력문에 end = " " 를 부여해서 엔터가 아닌 스페이스 형식으로 출력하면 됨.
print("===== 피드백 반영사항 =====")

for card in check_card_num:
    if card in have_card_num:
        print("1", end=" ")  # 있다면 1을 출력하고 띄어쓰기 유지
    else:
        print("0", end=" ")  # 없다면 0을 출력하고 띄어쓰기 유지
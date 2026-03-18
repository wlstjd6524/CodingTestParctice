'''
백준 1316: 그룹 단어 체커
URL : https://www.acmicpc.net/problem/1316
'''
num = int(input())
count = 0       # 그룹숫자 판별 count

for _ in range(num):    # 피드백 수용사항1) for i 로 선언시 word 의 마지막 수를 검사하지 않을 수 있음 따라서 i -> _ 로 치환
    word = input()
    check_list = []     # 피드백 수용사항2) 원래는 for 문 밖에 선언
    is_group = True     # 피드백 수용사항3) 일단 이 단어는 그룹단어 이겠지만 조건문을 따라서 아니면 False 로 치환해서 Count 를 올려줄 명목으로
    
    # 생각해 본 로직은 word 값을 check_list 에 하나씩 넣으면서 판별
    # 만약에 넣어보려고 하는 글자가 list 안에 있는거면 그건 그룹 단어가 아님 그래서 count 증감 x
    # 하지만, 연속된 알파벳이라면 그거는 상관이 없음 apply 는 그룹 단어가 맞음.

    # check_list.append(word[i]) 로 넣을건데.. 일단 0번째는 검사로직 체크없이 무조건 들어가야 하고
    # i 가 1인 순간부터는 검사로직이 돌아갸아함 -> 검사로직 : 1. 직전에 들어온 알파벳과 같은 알파벳인지? , 2. 그런게 아니라면 현재 List 에 나와
    # 같은 값이 존재하는지?

    for char in word:   # 피드백 수용사항4) 위의 for 문이 돌아가는건 사용자가 단어를 이만큼 받을거기 때문에 선언된 for 문이고, 얜 검사하기 위한 for문
        # 1. 지금 뽑은 글자가 이미 바구니에 들어 있음
        if char in check_list:
            # 2. 어 근데 직전에 들어온 알파벳이랑 다르면 => 떨어져서 나타난거임
            if char != check_list[-1]:
                is_group = False
                break
        # 검사를 했는데 문제가 없으면 리스트에 append
        check_list.append(char)
    
    # 글자를 다 검열했는데도 is_group 이 변환되지 않은거면 -> 얘는 그룹숫자임
    if is_group:
        count += 1
    
print(count)
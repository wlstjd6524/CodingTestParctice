'''
백준 1157: 단어 공부
URL : https://www.acmicpc.net/problem/1157
'''

'''
처음 접근법
pocket = "" 
pocket_num = 0      # 나중에 많이 사용된 알파벳을 출력하기 위한 저장 문자열 과 제일 많이 나온 알파벳 숫자를 하나씩 카운트 하면서
                    # 이 숫자가 제일 높은걸 출력하면 최대 빈도 알파벳을 출력할 수 있다고 생각하고 선언
for i in range(len(string)):
    if string[i] == string[i+1]:
        pocket = string[i]
        pocket_num += 1

다 짜본건 아니고 여기까지 생각을 해봤고 이런식의 접근을 진행하려고 했는데 이렇게 하면 머리속으로도 다음과 같은 사항을 야기 할 수 있었음

1. 조건문에서 분명 무조건 list 범위를 벗어났다는 에러가 발생할거임. 왜냐하면 결국엔 마지막 문장과 마지막 다음문장? 을 비교하라는 건데 그건 말이
안되니까

2. 그 다음 머리속으로 조건은 부합하지만 이렇게 되면 전문자랑 다음문자만 비교하기 때문에 aacdc 이런식의 문장에서 c가 떨어져있다면 얘네를 중복문자
로 보지 않고 Count 를 하지 않을 거임 결론은 붙어있는 알파벳만 출력하니 문제의도와 방향성에 어긋나기 시작할거임


그래서 생각해 본 결과 얘는 내장함수를 사용하는게 분명하다고 생각함.
'''
word = input().upper()      # 1. 대소문자를 신경쓰지 않는다고 했으니까 입력받는 값을 upper() 함수로 죄다 대문자로 바꿔버리기
letters = list(set(word))   # 2. set() 이라는 함수를 통해 중복을 제거 하고 남은 알파벳을 List 화 시켜두기

cnt_list = []
for char in letters:        # 파이썬 다운 코드 for i in range(len(letters)) 에서 문자열을 하나씩 그대로 꺼내볼 수 있는 형식으로 전환.
    cnt_list.append(word.count(char))

max_cnt = max(cnt_list)
if cnt_list.count(max_cnt) > 1:
    print("?")
else:
    # 1등이 있는 방 번호(인덱스)를 먼저 찾고
    max_index = cnt_list.index(max_cnt)  
    
    # letters 바구니에서 그 방 번호에 있는 알파벳을 출력!
    print(letters[max_index])
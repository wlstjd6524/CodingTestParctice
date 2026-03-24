'''
백준 9012: 괄호
URL : https://www.acmicpc.net/problem/9012
'''
# 문제의 규칙을 찾아보니 입력된 '(' 이랑 ')' 갯수가 서로 같으면 대칭으로 판단해서 VPS True / False 를 나누는 기준 같음
# 그니까 즉, (()) 는 각 2개씩 배치되니까 Yes 를 출력해야 되고 (())) 이거는 ( <- 얘는 두개고, ) <- 얘는 3개니까 NO 인 기준점.

# 피드백1. ↑ 처럼 생각하니 만약 )( 구조는 각각 1개씩 존재하는데 VPS 기준점에서는 No 임. 그럼 문제상 에러가 생김
# 피드백2. 접근법을 보니 ) 가 나올 때 반드시 그 앞에 짝을 지어 줄 ( 가 대기하고 있는가가 문제의 로직임.

T = int(input())
word_list = list()

for _ in range(T):
    word_list.append(input())

# 입력 다 받았으면 이제 하나씩 꺼내서 문자를 짜르고 대칭 구조가 맞는지 판별
for word in word_list:
    count = 0       # 단어가 바뀔 때마다 카운터는 0으로 초기화 해서 문자를 하나씩 구별해야 됨.
                    # count 를 선언한 이유는 ) 가 나올 때 +1 을 해주고 ( 가 나올 때는 -1 을 해주는 형식으로 검사를 함
                    # 그런데 count 가 음수가 되버리면 그건 짝이 맞지 않는 케이스에서 뭔가가 하나 더 나온 경우 이므로 무조건 탈락임
    
    for char in word:
        if char == '(':
            count += 1
        elif char == ')':
            count -=1
        
        if count < 0:
            break
    
    if count == 0:
        print("YES")
    else:
        print("NO")
    
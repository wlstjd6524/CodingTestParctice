'''
백준 2675: 문자열 반복
URL : https://www.acmicpc.net/problem/2675
'''
num = int(input())

for _ in range(num):                            # 피드백1) i 를 쓰는 구조가 없으니 i 대신 _ 로 대입
    word_result = ""

    word_num, word = input().split()
    word_num = int(word_num)

    for char in word:                           # 피드백2) j 를 쓰는 형태가 아니라 그냥 바구니 안에 있는걸 일일이 비교하는 로직인 char in 바구니 형태
        word_result += (char * word_num)        # 자꾸 까먹어서 기억할 때가 왔다.

    # for j in range(word_num):
        # word_result += (word[j] * word_num)   # 이런식의 구조를 취하다 보니 만약 5 /HTP 식처럼 word_num 의 수가 들어오는 단어수보다 많으면
                                                # for 문 구조에서 만약 4번째 인덱스를 추출하려고 String 문에 접근했는데, 문자가 없으니까
    print(word_result)                          # 범위 문제를 야기할 수 있음
                                                # 그렇다고 조건문을 달아보려고 했는데 -> 만약에 지금 현재 들어와있는 j 의 수가 문자열 len() 으로
                                                # 비교했을 때 더이상 값을 찾을 수 없으면 for 문 강제 break 해서 문자열을 더이상 안넣고 
                                                # 바로 출력하는 형식, 근데 여기서부터 막혔음. 분명.. 이런 복잡한 구조보다는 단순한 구조가 있을거라고 생각함.
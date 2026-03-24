'''
백준 1181: 단어 정렬
URL : https://www.acmicpc.net/problem/1181
'''
N = int(input())
word = set()                # 중복을 제거하려고 set 을 선언했고

for _ in range(N):
    word.add(input())       # 입력값 마다 set 에 넣어주고

word_list = list(word)      # 순서정렬을 다시 해주려고 list 로 감싼 걸 새로운 변수에 넣고
word_list.sort()            # 일단 사전 순으로 정렬

                            # 그다음에 리스트 안에 있는 걸알파벳 순으로 정렬을 하려고 하는데 
                            # for 문을 하나 더 돌려서 각자 인덱싱의 len 값을 비교해서 더 작은 len 이 맨 앞으로 가는 구조
                            # 길이를 정렬하는 다른 함수적 요소가 존재하나..? len 값을 직접 하자니 for 문에서 범위에러가 발생할 것 같음

word_list.sort(key=len)     # 피드백1. 실제로 길이를 정렬해주는 요소가 존재했음 sort(key=len)
                            # 피드백2. 지금 보면 sort 형식이 2개가 존재함 하나는 사전 순 정렬, 하나는 길이값에 대한 정렬 이걸 람다로 표현할 수 있음
                            # => word_list.sort(key=lambda x: (len(x), x))
                            # 해석 : 1순위는 길이로 정렬, 2순위는 알파벳 사전 순으로 정렬하는 한 줄의 코드로 경량화.
for w in word_list:
    print(w)
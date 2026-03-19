'''
백준 10809: 알파벳 찾기
URL : https://www.acmicpc.net/problem/10809
'''
find_num = 0        # while 문으로 반복문 돌릴 때 쓸 조건 변수
word_total = ""     # 출력문을 붙일 String 형 변수
word = input()


while find_num < 26:
    # 규칙이 존재했는데, 처음에는 word.find("a") 를 해서 a 를 찾은 결과를 word_total+= 형태로 붙이고
    # 그다음에 .find() 는 어차피 단어를 못찾으면 -1 을 리턴함.
    # 이거를 아스키코드 형식을 매핑해서 일일이 a,b,c,d 를 다는게 아니라 a 에 다음 아스키코드는 b 이니까 앞서 find 한거에 +1 값을 하면됨.

    alphabet = chr(97 + find_num)                   # 아스키코드 형태로 뽑아주는 chr()

    word_total += str(word.find(alphabet)) + " "    # 문자형 변환하고 공백 + " "

    find_num += 1

print(word_total)
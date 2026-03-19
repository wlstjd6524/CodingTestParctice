'''
백준 1543: 문서 검색
URL : https://www.acmicpc.net/problem/1543
'''
text = input()
user_text = input()
count = 0

text = text.replace(user_text, '*')

for char in text:
    if char == '*':
        count += 1

print(count)

# 백준 컴파일 완료, 소요시간 : 10분
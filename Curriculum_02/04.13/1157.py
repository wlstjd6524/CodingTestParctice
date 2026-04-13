'''
백준 1157: 단어 공부
URL : https://www.acmicpc.net/problem/1157
'''
word = input()

# 입력 받은 부분을 대문자로 승격
word = word.upper()

# count 랑 챔피온 변수를 하나 지정해야 하는데
# 이렇게 생각한 이유는 count 는 문자가 같으면 count ++ 로 올려서 제일 높은 count 를 가진 알파벳을 추출하려는 형식이고
# 챔피온 변수는 비교를 위한 챔피온 변수가 필요함

# 그래서 이번에도 set() 을 이용해 중복을 제거하는 형식으로
unique_letters = list(set(word))

# 알파벳 득표수를 저장할 리스트
count_list = []

for char in unique_letters:
    cnt = word.count(char)
    count_list.append(cnt)

# 챔피언 찾기
max_count = max(count_list)

# 예외조건, 문자열이 동률이 나오면 ? 로 출력하는
if count_list.count(max_count) > 1:
    print("?")
else:
    max_index = count_list.index(max_count)
    print(unique_letters[max_index])
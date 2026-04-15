'''
백준 1316: 그룹 단어 체커
URL : https://www.acmicpc.net/problem/1316
'''
word_count = int(input())
check_count = 0         # 만약 for 문 로직에서 해당 단어가 그룹 단어면 check_count 에 1씩 증감해서 마지막 출력에 check_count 갯수가 곧 그룹단어 수

for i in range(word_count):
    word = input()                      # 단어를 받고
    # word_list = []                    # 받은 단어를 Split 해서 넣을 빈 리스트를 생성 | 피드백1. for char in word: 형식이 이미 단어를 하나씩 뽑아줌
    
    # 두가지 메모리 영역 공간이 필요함
    # 1. 과거에 이 알파벳이 나왔나? 를 저장하는 리스트와
    # 2. 직전 알파벳을 비교할 단어장
    seen = []
    prev_char = ""

    for char in word:                   # 받은 단어를 하나씩 char 에 옮겨서
        # word_list.append(char)        # char 에 받은 split 단어를 빈 리스트에 집어넣고 | 피드백2. word_list 가 없어졌으니 없어져도 됨.
        if char != prev_char:
            if char in seen:
                break
            else:
                seen.append(char)

        # 다음 바퀴 돌기 전에 현재 알파벳을 방금 전 알파벳으로 돌려놔야 다음 알파벳이랑 비교가 가능
        prev_char = char

    # for-else 구문, 즉 for 문이 break 로 끊기지 않고 다 돌았을 대 else 블록이 실행 됨.
    # break 로 끊기지 않았다는건 그룹단어라는 의미이니까 check_count 에 증감
    else:
        check_count += 1

print(check_count)

'''
    for j in range(len(word_list)):     # word_list 만큼 반복문을 돌리는데
        # 의문점1. aabba 같은 케이스는 그룹단어가 아님 마지막에 이미 반복된 a가 혼자서 또 나오는 케이스 이기 때문에
        # 그래서 기억을 하려면 여기서 for 문을 하나 돌림 이유는 첫 번째 for 문에서 j 에 word_list[0] 번째 인덱스를 인덱싱 한 상태에서
        # 배열에 나머지 값을 다 비교함. 근데 word_list[0] 에서 연속되는 값들이 같은건 상관이 없는데 떨어져있는 값이 발견되면 걔는 그룹단어가 아님
        # 2중 for 문을 걸쳐서 그룹단어가 아니면 break 를 걸어버리고, 얘가 끝까지 돈다면 check_count 에 += 1 을 해서 이 단어는 그룹단어임을 나타내고
        # 마지막에 check_count 를 출력
        
        # 근데.. 어떻게 떨어져있는걸 구분해야하지.. 챔피언 변수에 지정하고 넣어야 하는지 감이 안잡힘.
'''
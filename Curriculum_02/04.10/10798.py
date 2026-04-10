'''
백준 10798: 세로읽기
URL : https://www.acmicpc.net/problem/10798
'''
result_list = []

# 5줄로 이루어진다 했으니까 5번 반복, 그리고 append 안에 list 를 또 부여해서 2중 List 로
for _ in range(5):
    result_list.append(list(input()))

# 개념은 어차피 5번 반복이니까 2중 리스트에 세로 대로 읽는 것도 5번 반복해서 읽으면 됨.
# 로직은 for 문을 돌리는데 result_list[i] 번째 인덱스들을 다 뽑을 거임 그럼 순서대로 출력?

'''
for i in range(5):              # 이렇게 하면 2중 리스트에서 처음 리스트로 진입하고
    for j in range(5):          # 여기서 처음 리스트로 진입 한 상태의 그 다음 리스트 안으로 들어감 여기서 인덱싱으로 값들을 추출 할 수 있음
        print(result_list[i][j], end = " ") 
'''

# 리스트 마다 들어가는 각 단어의 길이가 1 부터 15 까지 제멋대로 이기 때문에 최상단 for 문이 15번 돌아야 됨.
for j in range(15):
    for i in range(5):
        # 여기서 현재 줄(i) 의 길이가 지금 읽으려는 세로 위치(j) 보다 길 때만 읽는 형식으로
        # ex: 단어가 3글자 이면 인덱스 0, 1, 2 까지만 있고 3부터는 안 읽고 패싱
        if j < len(result_list[i]):
            # end="" 로 줄바꿈 없이, 띄어쓰기 없이 쭉 이어서 출력
            print(result_list[i][j], end="")
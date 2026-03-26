'''
백준 7568: 덩치
URL : https://www.acmicpc.net/problem/7568
'''

people_num = int(input())
people = []

# information 이라는 딕셔너리에 정보를 우겨 넣을 for 문
for _ in range(people_num):
    # 의문점1. 딕셔너리 형태는 어떤식으로 입력받을 수 있는가?
    # information = input()

    # 피드백1. key, value 에서 key 값의 형태는 보통 이름을 뽑아오는 요소로 많이 사용하기 때문에 딕셔너리 구조가 일단 필요가 없다.
    w, h = map(int, input().split())
    people.append((w,h))

# for 문을 통해 딕셔너리 형태의 key, value 를 받아오면
# 비교 for 문 작성
# 로직은, for 문을 돌리는데 조건문을 달아주는거임. 그 조건은 덩치가 큰 사람의 조건은 어떤 key 값과 어떤 value 와 비교해도 두개의 값이 다 큰 사람이
# 제일 덩치가 큰거임 그니까 조건문에 and 를 달아서 두개를 다 통과해야 그 사람의 ranking_count 값을 그대로 전달해주는 로직이고
# 만약에 몸무게는 큰데 키가 작아 그거는 조건문에 애초에 통과가 안되니까 그 사람들은 ranking_count ++ 한 값을 부여하는거임

# 의문점2. 보니까 공동 2등의 경우의 로직을 어떻게 처리해야하고, 이게 공동 2등 이 3명이 발생하고 참여자 수가 5명이면.. 다음이 3등이 아니라 바로 5등
# 그럼 사람수를 반영하는 부분도 구현이 되어야 하는가..

# 피드백2. 첫 번째 사람부터 마지막 사람까지 한 명씩 기준으로 잡고 for 문 돌리기
for i in range(people_num):
    rank = 1    # 일단 내 덩치 등수는 1등으로 일단 시작하고,

    # 피드백3. 기준인 나를 나머지 모든 사람이랑 1:1 로 비교해보고
    for j in range(people_num):

        # 로직으로 던졌던 몸무게도 커야하고 키도 커야 그 사람이 덩치가 제일 큰거다 => And 로직
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank += 1       # 이 조건을 부합하면 나보다 큰거니까 발견시 등수가 하나씩 밀림

    print(rank, end=" ")
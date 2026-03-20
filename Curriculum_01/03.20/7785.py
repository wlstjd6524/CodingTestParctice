'''
백준 7785: 회사에 있는 사람
URL : https://www.acmicpc.net/problem/7785
'''

'''
log_record = int(input())

for i in range(log_record):
    name, enle = list(input().split())

    if enle[i] == "leave":
        name = name[i].replace('*')
    
for j in range(len(name)):
    if name[j] != '*':
        print(name[j])
'''

# 구조는 이런느낌으로 진행
# 반복문을 처음으로 돌릴 숫자를 받고 이름이랑 지금 들어와있는지, 없는지에 대한 여부를 list 로 받기
# 근데 만약에 들어온 값이 leave 면 빠져나간거니까 그 사람 이름은 * 로 대체
# 이제 *로 대체되었으니 * 의 이름을 가진 사람은 빠져나간거임 그래서 name 에서 *이 아닌 사람 즉, 회사에 들어와있는 사람에 이름을 출력

# 근데 문제점이 발생한게 일단 마지막 사람의 글자가 하나씩 쪼개지며서 나오게 되고,
# 무엇보다 뭔가 들어오는 형태가 Key:Value 값 형태여서... 딕셔너리를 활용하면 어떨까 라는 생각이 들었음.

'''
피드백

1. for 문 안에 name, enle = list(input().split()) 로 받고 인덱스 형식으로 선언이 안되서 계속 새로운 데이터가 덮어쓰기가 됐음
2. 중요한건 두번째에 조건 문에는 인덱싱을 넣었다는거임. 이렇게 하면 들어온 문자를 잘게 쪼개버림 if enle = "leave" 가 맞는 형태였음
3. 무엇보다 존재하는 느낌이 Key:Value 값이라는 걸 보아서 딕셔너리 형태로 선언하고 받아들이는게 맞았음
'''

print('======== 피드백 반영사항 수정 코드 ========')
log_record = int(input())
company = {}

for _ in range(log_record):
    name, enle = input().split()

    if enle == "enter":
        company[name] = "enter"
    else:
        del company[name]

# 이제 남아있는 사람들의 이름(Key)만 뽑아서 역순(Z-A)으로 정렬해야함
# company.keys()는 딕셔너리의 Key(이름)들만 모아주는 유용한 함수
survivors = sorted(company.keys(), reverse=True)

# 정렬된 명단 한줄씩 출력
for person in survivors:
    print(person)
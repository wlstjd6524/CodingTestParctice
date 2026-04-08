'''
백준 3040: 백설 공주와 일곱 난쟁이
URL : https://www.acmicpc.net/problem/3040
'''
# 9명 중에 7명을 뽑는 것 보다, 9명 중 2명을 탈락시키면 접근법이 조금 더 쉬움.
miniboy_list = []

fake_miniboy1 = 0
fake_miniboy2 = 0

# 일단 9명을 miniboy_list 에 집어넣고
for _ in range(9):
    miniboy_list.append(int(input()))

# 피드백1. 두명을 빼서 100이 되는지 확인하려면 일단 9명 전체 합의 키를 알고 있어야 됨.
total_sum = sum(miniboy_list)

# 2중 for 문을 통해서 어떤 특정 숫자가 더해지면 100 이 안되는 숫자가 2개 존재할건데
# 그 2개가 가짜 난쟁이니까 그 각 2개의 숫자를 fake_miniboy1 이랑 2에 대입
# 결국 for i 문에서 하나, j 문에서 하나씩 발생하는 구조가 되는건가?

'''
for i in range(9):
    for j in range(9):
'''
# 피드백2. 처음에는 위 for 문 처럼 구현하려고 했으나 이렇게 될 경우 같은 난쟁이를 가르키기 때문에 두 번째 for 문에서는 첫 번째 for 문이 가르킨
# 난쟁이를 가르키지 않도록 범위를 지정해야 된다고 함.
for i in range(9):
    for j in range(i + 1, 9):
        # 전체 합에서 지금 고른 두명(i번째, j번째) 의 키를 빼니까 딱 100 이라면?
        if total_sum - (miniboy_list[i] + miniboy_list[j]) == 100:
            fake_miniboy1 = miniboy_list[i]
            fake_miniboy2 = miniboy_list[j]

# 가짜 난쟁이는 이제 fake_miniboy 1과 2에 각각 저장되었으니까 진짜 난쟁이들만 남게 가짜 난쟁이 두명을 9명 리스트에서 제거
miniboy_list.remove(fake_miniboy1)
miniboy_list.remove(fake_miniboy2)

# 이제 리스트에 남은 난쟁이가 진짜 난쟁이들이니까 한 줄씩 출력
for dwarf in miniboy_list:
    print(dwarf)
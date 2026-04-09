'''
백준 3040: 백설 공주와 일곱 난쟁이
URL : https://www.acmicpc.net/problem/3040
'''
miniboy_list = []

for _ in range(9):
    miniboy_list.append(int(input()))

total_height = sum(miniboy_list)

fake_miniboy1 = 0
fake_miniboy2 = 0

for i in range(9):
    for j in range(i+1, 9):
        if total_height - (miniboy_list[i] + miniboy_list[j]) == 100:
            fake_miniboy1 = miniboy_list[i]
            fake_miniboy2 = miniboy_list[j]

miniboy_list.remove(fake_miniboy1)
miniboy_list.remove(fake_miniboy2)

for k in miniboy_list:
    print(k)
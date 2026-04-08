'''
백준 2566: 최댓값
URL : https://www.acmicpc.net/problem/2566
'''
# 어렵다고 생각해서 복습 (보고 치는게 아니라 전 날 배운 로직을 생각해서 순수 타이핑)

board = []

for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

max_num = -1
max_row = 0
max_col = 0

for i in range(9):
    for j in range(9):
        if board[i][j] > max_num:
            max_num = board[i][j]
            max_row = i + 1
            max_col = j + 1

print(max_num) 
print(max_row, max_col)
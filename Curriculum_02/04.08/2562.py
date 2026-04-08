'''
백준 2562: 최댓값
URL : https://www.acmicpc.net/problem/2562
'''
max_num = 0
count = 0

for i in range(9):
    num = int(input())
    
    if num > max_num:
        max_num = num
        count = i + 1

print(max_num)
print(count)
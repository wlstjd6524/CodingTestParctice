'''
백준 4673: 셀프넘버
URL : https://www.acmicpc.net/problem/4673
'''
del_list = set()

for i in range(1, 10001):
    num = i

    for char in str(i):
        num += int(char)

    del_list.add(num)

for i in range(1, 10001):
    if i not in del_list:
        print(i)
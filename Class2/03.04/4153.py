'''
- solved.ac Class1 - 백준 4153번 문제 (직각삼각형)

- [문제](https://www.acmicpc.net/problem/4153)
'''
while True:
    nums = list(map(int, input().split()))
    nums.sort()

    if nums[2] == 0:
        break
    elif (nums[2] ** 2) == (nums[0] ** 2) + (nums[1] ** 2):
        print('right')
    else:
        print('wrong')
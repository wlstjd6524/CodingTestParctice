'''
- solved.ac Class1 - 백준 3052번 문제 (음계)

- [문제](https://www.acmicpc.net/problem/3052)
'''
re_num = list()

for i in range(10):
    num = int(input())
    re_num.append(num % 42)

re_num = set(re_num)
print(len(re_num))

'''
1. 일단 빈 리스트를 선언하고 num[i] = num % 42 로 우겨넣으려고 했던 점 
    -> 빈 리스트를 선언한 다음에 이렇게 값을 우겨넣어버리면 파이썬 자체에서 공간을 찾을 수가 없어서 Error Return
    -> .append() 로 값 넣어주기

2. 값을 for 문으로 하나씩 비교해야 된다 생각함
    -> 근데 set() 의 경우 값을 받은 List 에서 중복된 값을 제거해버림
    -> 그래서 남아 있는 값의 길이가 즉, 같은 숫자가 제거된 상태의 상태이니까 문제에서 맞는 다른 수의 갯수를 Return 할 수 있음
'''
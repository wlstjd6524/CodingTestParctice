'''
백준 2908: 상수
URL : https://www.acmicpc.net/problem/2908
'''
a, b = input().split()

a = a[::-1]
b = b[::-1]

a = int(a)
b = int(b)

if a > b:
    print(a)
else:
    print(b)

# 백준 컴파일 완료, 소요시간 : 11분
# 고민했던 부분은 처음에는 정수형으로 받아서 그냥 뒤집어 보려고 했는데 정수형은 [::-1] 형태가 작동되지 않았음.
# 그다음 코드 경량화를 시킬 수 있을 것 같은데.. 일단 동작은 되니까 건드리지는 않았음

# 리뷰세션 : 실제로 경량화를 할 수 있었음 -> print(max(int(a[::-1]), int(b[::-1])))
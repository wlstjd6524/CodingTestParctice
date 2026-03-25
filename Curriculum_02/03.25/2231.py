'''
백준 2231: 분해합
URL : https://www.acmicpc.net/problem/2231
'''
# 개념적으로 보면 반복문을 통해서 처음에 x=1 식으로 변수를 할당 한 다음에
# 얘를 split 해서 x + x_split 한 값이 처음에 사용자가 입력한 값이랑 같으면 출력, 아니면 x 증감 식으로 하면
# X 의 최소값을 바로 찾을 수 있는데...
# 코드 로직이 너무 어렵다... 

N = int(input())
result = 0

for x in range(1, N+1):
    x_split = sum(map(int, str(x)))

    if x + x_split == N:
        result = x
        break

print(result)
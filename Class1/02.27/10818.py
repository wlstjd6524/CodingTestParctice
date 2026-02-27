'''
- solved.ac Class1 - 백준 10818번 문제 (최소, 최대)

- [문제](https://www.acmicpc.net/problem/10818)
'''
n = int(input())
num_list = list(map(int, input().split()))

max_num = num_list[0]
min_num = num_list[0]

for i in range(n):
    if num_list[i] > max_num:
        max_num = num_list[i]
    elif num_list[i] < min_num:
        min_num = num_list[i]

print(min_num, max_num)

'''
오늘도 나의 소중한 1시간 중에 20분을 뺏어간 문제였다.
로직 자체는 단순하기도 하고, 접근법도 어렵지 않았는데 문제는 내가 초기값을 잘 못 설정한 부분에 있었다.

최대값을 담을 그릇과 최소값을 담을 그릇을 처음에 0으로 설정을 했다.
어차피 어떤 값들이 들어와도 0 보다는 클테니까, 그런데 음수가 들어올 수도 있다는 가정을 완전히 무시하고 잡은 초기값이였다.

그래서 비교를 위한 List 의 첫 값을 공통으로 최대, 최소를 담을 그릇에 셋팅하고 시작했다. (이러면 음수도 값을 비교할 수 있었음)


그다음은 if, else 부분이였다.
처음에는 if num_list[i] > max_num 에 else 를 주면 그 반대인 로직을 전부 처리한다는 생각으로 if, else 값을 넘겨줬다.
그런데 else 를 줘버리면 등호의 반대개념만 처리하기 때문에 최소값을 구할 로직이 전혀 없다는 점이였다.

그래서 최소값을 넘겨주는 로직도 추가로 구현하였다.

이런 문제에 20분을 쓴게 자기반성이 조금 필요한 하루였다.
'''
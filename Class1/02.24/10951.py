'''
- solved.ac Class1 - 백준 10951번 문제 (A+B - 4)

Q. 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

Input : 입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

Print : 각 테스트 케이스마다 A+B를 출력한다.
'''
while True:
    try:
        A,B = map(int, input().split())
        print(A+B)
        pass
    except EOFError:
        break

# 문제를 고민했던 부분은 바로 반복문은 돌아가는데 어떤 시점에서 프로그램이 멈춰야 하는지에 대한 부분이였다.
# 그래서 생각한 부분이 try, except 였고, 근데 구체적으로 except 다음에 오는 에러명을 뱉어주는 요소를 알 수가 없었다.
# 그래서 LLM 을 활용하여 EOFError 를 학습했다.
# EOF(End of File) : 더 이상 읽어 들일 데이터가 없다 라는 상태, 이 상태에 도달시 더이상 읽을 프로그램이 없어 에러 반환.
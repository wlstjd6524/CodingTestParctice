'''
- solved.ac Class1 - 백준 1330번 문제 (두 수 비교하기)

Q. 두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.
'''

A, B = map(int, input().split())        # 변수를 한번에 받기 위해서 map() 으로 list 화를 시킨 후에 input() 으로 값을 받고
                                        # split() 으로 각 변수에 할당값을 쪼개주기

if A>B:
    print('>')
elif A<B:
    print('<')
else:
    print('==')
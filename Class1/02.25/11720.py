'''
- solved.ac Class1 - 백준 11720번 문제 (숫자의 합)

Q. N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

Input : 첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

Print : 입력으로 주어진 숫자 N개의 합을 출력한다.
'''

first_num = int(input())
second_num = list(map(int, input()))

sum = 0
for i in range(1, first_num+1):
    sum += second_num[i-1]

print(sum)
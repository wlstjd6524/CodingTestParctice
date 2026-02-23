'''
- solved.ac Class1 - 백준 10869번 문제 (사칙연산)

Q. 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
'''
a,b = input().split()
a = int(a)
b = int(b)

# 코드가 조금 지저분한데, map() 함수를 인지하고 수행능력을 인지한 상태로서 위에 코드를
# a, b = map(int, input().split()) 로 줄일 수 있겠다.

print(a+b)
print(a-b)
print(a*b)
print(int(a/b))
print(a%b)
'''
- solved.ac Class1 - 백준 10809번 문제 (알파벳 찾기)

- [문제](https://www.acmicpc.net/problem/8958)
'''
# .find() 함수 사용해보기
word = input()

for i in range(97, 123):
    alphabet = chr(i)
    print(word.find(alphabet), end=" ")
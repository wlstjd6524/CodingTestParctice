'''
- solved.ac Class1 - 백준 2675번 문제 (문자열 반복)

- [문제](https://www.acmicpc.net/problem/2675)
'''
test_num = int(input())

for i in range(test_num):
    total_word = ""
    word_num, word = input().split()
    word_num = int(word_num)
    
    for j in word:
        total_word += j * word_num
    
    print(total_word)
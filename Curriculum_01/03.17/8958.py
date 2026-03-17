'''
백준 8958: OX 퀴즈
URL : https://www.acmicpc.net/problem/8958
'''
test_caseNum = int(input())

for i in range(test_caseNum):
    sum = 0
    count = 0
    test_case = input()

    for j in range(len(test_case)):        # 의문점1. test_case 는 input() 으로 받았으니까 문자형 일거고 그에 해당하는 len 값이 주어질텐데
                                           # 그러면 그 len 값은 정수형이 아닌가? 왜 'int' object is not iterable 을 뱉어내어내는가?
        if test_case[j] == 'O':
            count += 1
            sum += count
        elif test_case[j] == 'X':
            count = 0
    print(sum)

# 의문점1 을 해결해보기 위해 for 문에 range() 를 돌리니까 정상적으로 동작했다.
# 그렇다면 range() 를 넣어야 하는 이유? -> 정확히는 for 문 구조에 대해서 정확히 알아볼 필요가 있겠다.
# 백준 컴파일 완료, 소요시간 : 18분
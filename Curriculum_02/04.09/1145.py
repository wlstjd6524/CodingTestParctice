'''
백준 1145: 적어도 대부분의 배수
URL : https://www.acmicpc.net/problem/1145
'''
# 입력 받기
num_list = list(map(int, input().split()))

result_num = 1
# 이제 이 밑에서 num_list 에 있는 모든 요소들이 result_num 이랑 나눠보는데
# 조건은 'num_list 에서 result_num 이랑 나눠떨어지는 수가 적어도 3개 이상 존재해야됨'
# 그리고 흐름로직은 이런식으로 해야됨. 일단은 list 수를 다 나눠보고 나눠지는 수가 3개 이상이면 그 수를 result_num 에 박고 밖으로 빼서 출력

# 피드백1. 정답이 나올 때 까지 for 문을 무한정 돌리는 로직으로 접근 할 필요가 있음
while True:
    count = 0

    for i in range(5):
        # if num_list[i] % result_num == 0:
        if result_num % num_list[i] == 0:       # 원래 셋팅했던 것이 위의 값인데 위의 값은 '배수' 를 찾는 것이 아니라 '약수' 를 찾는 것 이였음.
            count += 1

    if count >= 3:
        # result_num = i , 이렇게 지정하고 밖에서 result_num 을 출력하는 형식이였는데 피드백을 받고나서는 해당 사항이 만족하면 print 하고 
        # While 문 Break
        print(result_num)
        break
        
        # 피드백3. 3개가 안 된다면, 다음 숫자로 넘어가서 다시 처음부터 검사
    result_num += 1
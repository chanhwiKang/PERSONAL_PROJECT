def solution(number, limit, power):
    
    i = 0
    yaksu_cnt = []
    for knight in range(1, number+1): # knight의 수만큼 반복
        if number % knight == 0 :
            yaksu_cnt.append(knight)
    print(yaksu_cnt)
    for i in range(0, len(yaksu_cnt)): # 0 ~ 약수의 갯수까지
        if yaksu_cnt[i] > limit : # 약수의 갯수가 limit보다 크다면,
            del yaksu_cnt[i]
            yaksu_cnt.append(power)
                

    return sum(yaksu_cnt)

print(solution(10, 3, 2))
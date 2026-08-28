# 투포인터 학습하기

# 합이 10이 되는 두 수의 개수 찾기
numbers = [1,2,3,5,7,8,10,11]

def twoPointer(num_list, n):
    s_p = 0
    e_p = len(num_list)-1
    cnt = 0
    while s_p<e_p:
        two_sum = num_list[s_p]+num_list[e_p]
        if two_sum == n:
            cnt += 1
            e_p -= 1 # 엔드포인트 왼쪽으로
        elif two_sum < 10:
            s_p += 1
        else:
            e_p -= 1
    return cnt

print(twoPointer(numbers, 10))

"""
[정수론 - 최대공약수(GCD)와 최소공배수(LCM)]

문제 설명:
- 두 정수의 최대공약수(GCD)와 최소공배수(LCM)를 구합니다.
- 유클리드 호제법을 사용하여 GCD를 효율적으로 계산합니다.
- GCD를 이용하여 LCM을 계산합니다.

입력:
- a, b: 두 개의 양의 정수

출력:
- GCD: 최대공약수
- LCM: 최소공배수

예제:
입력: a = 48, b = 18
출력: 
  GCD = 6
  LCM = 144

힌트:
- 유클리드 호제법: gcd(a, b) = gcd(b, a % b)
- LCM 공식: lcm(a, b) = (a × b) / gcd(a, b)
"""

def gcd(a, b):
    """
    유클리드 호제법을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수
    """
    # TODO: 유클리드 호제법 구현
    # base case: b가 0이면 a 반환
    # recursive를 이용 
    if b==0:
        return a
    if a<b:
        a, b = b, a
    # print(a, b)
    return gcd(b, a%b)

def gcd_iterative(a, b):
    """
    반복문을 사용한 최대공약수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최대공약수
    """
    # TODO: 반복문으로 구현
    # b가 0이 될 때까지 반복
    if a<b:
        a,b = b,a
    while True:
        if b == 0:
            break
        a, b = b, a%b
    return a

def lcm(a, b):
    """
    최소공배수 계산
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        최소공배수
    """
    # TODO: LCM 계산
    return a*b//gcd(a, b)

def extended_gcd(a, b):
    """
    확장 유클리드 호제법
    ax + by = gcd(a, b)를 만족하는 x, y를 찾음
    
    Args:
        a, b: 두 양의 정수
    
    Returns:
        (gcd, x, y) 튜플
    """
    # TODO: 확장 유클리드 호제법 구현
    # base case: b가 0이면 (a, 1, 0) 반환    
    # recursive case
    # 역추적하며 x, y 계산
    if b == 0:
        return a, 1, 0 # 초기값 a=gcd, b=0일때 종료됨으로 ax+bx=gcd일떄 1, 0이 각각 x, y의 계수가됨
    r_gcd, x, y = extended_gcd(b, a%b)

    x1 = y
    y1 = x - (a//b) * y
    return r_gcd, x1, y1
    

def is_prime(n):
    """
    소수 판별   ``
    
    Args:
        n: 판별할 양의 정수
    
    Returns:
        소수이면 True, 아니면 False
    """
    # TODO: 소수 판별 구현
    # n이 2보다 작으면 False
    # 2부터 sqrt(n)까지 나누어 떨어지는지 확인    
    # 3부터 sqrt(n)까지 홀수만 확인
    from math import sqrt
    if n<2:
        return False
    elif n == 2:
        return True
    else:
        # 소수는 1, 자기자신을 약수로 가짐
        # n에 루트를 씌우면 나오는 수는 n의 약수중
        # n보다 작거나 같은 약수임 따라서 이수로 나뉘게 되면 n보다 큰 약수가 나오기 때문에
        # 굳이 n까지 안돌려봐도 답을 구할수 있음
        n_sqrt = int(sqrt(n))+1 
        # print(n_sqrt)
        if n % 2 == 0:
            return False
        else:
            for i in range(3, n_sqrt, 2):
                # print(i)
                if n%i == 0:
                    return False
            return True

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: GCD와 LCM
    print("=== 테스트 케이스 1: GCD와 LCM ===")
    a, b = 48, 18
    print(f"a = {a}, b = {b}")
    print(f"GCD (재귀): {gcd(a, b)}")
    print(f"GCD (반복): {gcd_iterative(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 2
    print("=== 테스트 케이스 2 ===")
    a, b = 100, 75
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print()
    
    # 테스트 케이스 3: 서로소
    print("=== 테스트 케이스 3: 서로소 ===")
    a, b = 17, 19
    print(f"a = {a}, b = {b}")
    print(f"GCD: {gcd(a, b)}")
    print(f"LCM: {lcm(a, b)}")
    print("서로소(coprime): GCD가 1")
    print()
    
    # 테스트 케이스 4: 확장 유클리드
    print("=== 테스트 케이스 4: 확장 유클리드 ===")
    a, b = 35, 15
    g, x, y = extended_gcd(a, b)
    print(f"a = {a}, b = {b}")
    print(f"GCD = {g}")
    print(f"{a} × {x} + {b} × {y} = {g}")
    print(f"검증: {a * x + b * y} = {g}")
    print()
    
    # 테스트 케이스 5: 소수 판별
    print("=== 테스트 케이스 5: 소수 판별 ===")
    test_numbers = [2, 3, 4, 17, 20, 29, 100]
    for num in test_numbers:
        result = "소수" if is_prime(num) else "합성수"
        print(f"{num}: {result}")



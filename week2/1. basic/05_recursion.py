"""
[재귀 함수 - 팩토리얼과 피보나치 수열]

문제 설명:
- 재귀 함수를 사용하여 팩토리얼과 피보나치 수를 계산합니다.
- 재귀의 기본 개념인 base case와 recursive case를 이해합니다.

입력:
- n: 양의 정수

출력:
- 팩토리얼: n!
- 피보나치: n번째 피보나치 수

예제:
입력: n = 5
팩토리얼 출력: 120 (5! = 5 x 4 x 3 x 2 x 1)
피보나치 출력: 5 (0, 1, 1, 2, 3, 5)

힌트:
- 팩토리얼: n! = n x (n-1)!, 0! = 1
- 피보나치: fib(n) = fib(n-1) + fib(n-2), fib(0) = 0, fib(1) = 1
"""

def factorial(n):
    """
    재귀를 사용한 팩토리얼 계산
    
    Args:
        n: 양의 정수
    
    Returns:
        n의 팩토리얼 값
    """
    # TODO: base case를 작성하세요
    # n이 0이거나 1이면 1을 반환
    if n < 1: # 0! = 1
        return 1

    return n*factorial(n-1)
    
    # TODO: recursive case를 작성하세요
    pass

def fibonacci(n):
    """
    재귀를 사용한 피보나치 수 계산
    
    Args:
        n: 구하고자 하는 피보나치 수의 인덱스
    
    Returns:
        n번째 피보나치 수
    """
    # TODO: base case를 작성하세요
    # n이 0이면 0, n이 1이면 1 반환
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
    
    # TODO: recursive case를 작성하세요

# 테스트 케이스
if __name__ == "__main__":
    # 팩토리얼 테스트
    print("=== 팩토리얼 계산 ===")
    for i in range(6):
        result = factorial(i)
        print(f"{i}! = {result}")
    print()
    
    # 피보나치 테스트
    print("=== 피보나치 수열 ===")
    for i in range(10):
        result = fibonacci(i)
        print(f"fib({i}) = {result}")
    print()
    
    # 추가 테스트
    print("=== 추가 테스트 ===")
    print(f"10! = {factorial(10)}")
    print(f"fib(15) = {fibonacci(15)}")



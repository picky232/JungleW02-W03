"""
[분할 정복 - 배열의 최댓값 찾기]

문제 설명:
- 분할 정복(Divide and Conquer) 방식으로 배열의 최댓값을 찾습니다.
- 배열을 반으로 나누고, 각 부분의 최댓값을 구한 후 비교합니다.

입력:
- arr: 정수 배열
- left: 시작 인덱스
- right: 끝 인덱스

출력:
- 배열의 최댓값

예제:
입력: [3, 5, 1, 8, 2, 9, 4]
출력: 9

힌트:
- Base case: left == right일 때 arr[left] 반환
- 배열을 반으로 나누어 재귀 호출
- 왼쪽과 오른쪽의 최댓값 중 큰 값 반환
"""

def find_max_divide_conquer(arr, left, right):
    """
    분할 정복으로 최댓값 찾기
    
    Args:
        arr: 배열
        left: 시작 인덱스
        right: 끝 인덱스
    
    Returns:
        최댓값
    """
    # TODO: base case - 원소가 하나면 그 값 반환
    if len(arr) == 1:
        return arr[0]
    
    # TODO: 중간 지점 계산
    mid = (left+right)//2
    
    # TODO: 왼쪽 절반의 최댓값
    l_max = max(arr[left:mid])
    left_arr = arr[left:mid]
    # TODO: 오른쪽 절반의 최댓값
    r_max = max(arr[mid:right+1])
    right_arr = arr[mid:right+1]

    # TODO: 둘 중 큰 값 반환
    if l_max > r_max:
        return find_max_divide_conquer(left_arr, 0, mid)
    else:
        return find_max_divide_conquer(right_arr, 0, mid+1)

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [3, 5, 1, 8, 2, 9, 4]
    result1 = find_max_divide_conquer(arr1, 0, len(arr1) - 1)
    print(f"배열: {arr1}")
    print(f"최댓값: {result1}")
    print()
    
    # 테스트 케이스 2
    arr2 = [10, 20, 30, 40, 50]
    result2 = find_max_divide_conquer(arr2, 0, len(arr2) - 1)
    print(f"배열: {arr2}")
    print(f"최댓값: {result2}")
    print()
    
    # 테스트 케이스 3
    arr3 = [100]
    result3 = find_max_divide_conquer(arr3, 0, len(arr3) - 1)
    print(f"배열: {arr3}")
    print(f"최댓값: {result3}")



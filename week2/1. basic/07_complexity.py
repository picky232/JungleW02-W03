"""
[복잡도 분석 - Big O, 시간 복잡도, 공간 복잡도]

문제 설명:
- 여러 알고리즘의 시간 복잡도와 공간 복잡도를 이해하고 비교합니다.
- 동일한 문제를 다른 복잡도로 해결하는 방법을 학습합니다.
- 배열에서 중복 원소를 찾는 문제를 여러 방법으로 구현합니다.

입력:
- nums: 정수 배열

출력:
- 중복된 원소들의 리스트

예제:
입력: [4, 3, 2, 7, 8, 2, 3, 1]
출력: [2, 3]

힌트:
- 방법1: 이중 반복문 (O(n²) 시간, O(1) 공간)
- 방법2: 정렬 후 탐색 (O(n log n) 시간, O(1) 공간)
- 방법3: 해시 집합 사용 (O(n) 시간, O(n) 공간)
"""

def find_duplicates_brute_force(nums):
    """
    방법1: 이중 반복문 사용
    시간 복잡도: O(n²)
    공간 복잡도: O(k) - k는 중복 원소 개수
    """
    duplicates = []
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            # print(nums[i], nums[j])
            if nums[i] == nums[j]:
                # print("1")
                if nums[i] not in duplicates:
                    duplicates.append(nums[i])
    # print(duplicates)
    
    # TODO: 이중 반복문으로 중복 찾기
    ## i번째 원소와 i+1 이후의 모든 원소를 비교
    ## 같은 원소를 찾으면 duplicates에 추가 (중복 추가 방지 필요)
    
    return duplicates

def find_duplicates_sorting(nums):
    """
    방법2: 정렬 후 인접 원소 비교
    시간 복잡도: O(n log n) - 정렬
    공간 복잡도: O(1) - 정렬을 in-place로 수행
    """
    if not nums:
        return []
    
    # TODO: 배열을 정렬하세요 (nums.sort() 사용)
    pass
    
    duplicates = []
    
    # TODO: 인접한 원소를 비교하여 중복 찾기
    # i와 i+1 원소가 같고, duplicates에 없으면 추가
    pass
    
    return duplicates

def find_duplicates_hash(nums):
    """
    방법3: 해시 집합 사용
    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    seen = set()
    duplicates = set()
    
    # TODO: 각 원소를 순회하면서
    ## 이미 seen에 있으면 duplicates에 추가
    ## 없으면 seen에 추가
    pass
    
    return list(duplicates)

def measure_time(func, nums, method_name):
    """실행 시간 측정 헬퍼 함수"""
    result = func(nums[:])  # 복사본 전달
    print(f"{method_name}: {sorted(result)}")
    print()

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 작은 배열
    print("=== 테스트 케이스 1: 작은 배열 ===")
    nums1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"입력: {nums1}\n")
    
    result1 = find_duplicates_brute_force(nums1)
    print(f"방법1 (Brute Force): {sorted(result1)}")
    
    result2 = find_duplicates_sorting(nums1)
    print(f"방법2 (Sorting): {sorted(result2)}")
    
    result3 = find_duplicates_hash(nums1)
    print(f"방법3 (Hash): {sorted(result3)}")
    print()
    
    # 테스트 케이스 2: 큰 배열로 성능 비교
    print("=== 테스트 케이스 2: 성능 비교 (n=1000) ===")
    import random
    random.seed(42)  # 동일한 결과를 위한 시드 설정
    nums2 = [random.randint(1, 500) for _ in range(1000)]
    
    measure_time(find_duplicates_brute_force, nums2, "방법1 (O(n²))")
    measure_time(find_duplicates_sorting, nums2, "방법2 (O(n log n))")
    measure_time(find_duplicates_hash, nums2, "방법3 (O(n))")
    
    print("=== 복잡도 분석 요약 ===")
    print("방법1 - Brute Force:")
    print("  시간: O(n²), 공간: O(k)")
    print("  특징: 간단하지만 느림")
    print()
    print("방법2 - Sorting:")
    print("  시간: O(n log n), 공간: O(1)")
    print("  특징: 추가 메모리 없이 효율적")
    print()
    print("방법3 - Hash:")
    print("  시간: O(n), 공간: O(n)")
    print("  특징: 가장 빠르지만 메모리 사용")



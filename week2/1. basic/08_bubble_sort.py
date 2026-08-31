"""
[버블 정렬 구현]

문제 설명:
- 버블 정렬(Bubble Sort) 알고리즘을 구현합니다.
- 인접한 두 원소를 비교하여 정렬하는 방식입니다.
- 가장 큰 원소가 배열의 끝으로 "버블"처럼 이동합니다.

입력:
- arr: 정렬되지 않은 정수 배열

출력:
- 오름차순으로 정렬된 배열

예제:
입력: [64, 34, 25, 12, 22, 11, 90]
출력: [11, 12, 22, 25, 34, 64, 90]

힌트:
- 외부 반복문: n-1번 실행
- 내부 반복문: 인접한 원소 비교 및 교환
- 최적화: 교환이 없으면 이미 정렬된 것이므로 조기 종료
"""

def bubble_sort(arr):
    """
    버블 정렬 구현
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)
    
    # TODO: 외부 반복문 - n-1번 반복
    # 각 패스마다 가장 큰 원소가 끝으로 이동

    cnt = 0
    for i in range(n-1):
        # turn = True
        for j in range(n-i-1):
            cnt += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # turn = False
            # print(arr, cnt)
        # if turn:
        #     break
            
    

    ## TODO: 내부 반복문 - 인접한 원소 비교
    ## 0부터 n-i-1까지 반복 (이미 정렬된 뒷부분 제외)
    ## TODO: 인접한 두 원소 비교 및 교환
    ## arr[j] > arr[j+1]이면 교환
    ## 외부 반복문: n-1번 실행
        
    return arr

def bubble_sort_optimized(arr):
    """
    최적화된 버블 정렬 (조기 종료 포함)
    
    Args:
        arr: 정렬할 배열
    
    Returns:
        정렬된 배열
    """
    n = len(arr)
    
    for i in range(n-1):
        swapped = True  # 교환 발생 여부
        
        # TODO: 내부 반복문과 교환 로직 구현
        # 교환이 발생하면 swapped = True 설정
        cnt = 0      
        for j in range(n-1-i):
            cnt += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            # print(cnt)
        if swapped:
            break

        # TODO: 교환이 없으면 이미 정렬된 것이므로 break

    return arr

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print("=== 테스트 케이스 1 ===")
    print(f"정렬 전: {arr1}")
    result1 = bubble_sort(arr1.copy())
    print(f"정렬 후: {result1}")
    print()
    
    # 테스트 케이스 2: 이미 정렬된 배열
    arr2 = [1, 2, 3, 4, 5]
    print("=== 테스트 케이스 2: 이미 정렬됨 ===")
    print(f"정렬 전: {arr2}")
    result2 = bubble_sort_optimized(arr2.copy())
    print(f"정렬 후: {result2}")
    print("최적화 버전은 1번의 패스만 수행")
    print()
    
    # 테스트 케이스 3: 역순 배열
    arr3 = [5, 4, 3, 2, 1]
    print("=== 테스트 케이스 3: 역순 ===")
    print(f"정렬 전: {arr3}")
    result3 = bubble_sort(arr3.copy())
    print(f"정렬 후: {result3}")



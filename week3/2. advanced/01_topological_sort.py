"""
[위상 정렬 - Topological Sort]

문제 설명:
- 방향 그래프에서 순서를 정합니다.
- 선행 작업이 먼저 오도록 정렬합니다.
- 예: 과목 선수과목, 작업 순서

입력:
- graph: 방향 그래프
- vertices: 정점 개수

출력:
- 위상 정렬 순서

예제:
과목:
0(기초) → 1(중급) → 3(고급)
0(기초) → 2(응용)

위상 정렬: [0, 1, 2, 3] 또는 [0, 2, 1, 3]

힌트:
- 진입 차수(in-degree) 사용
- 진입 차수가 0인 정점부터 시작
- 큐 사용
"""

from collections import deque

def topological_sort(vertices, edges):
    """
    위상 정렬 (Kahn's Algorithm)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
    
    Returns:
        위상 정렬 순서
    """
    # TODO: 그래프와 진입 차수 초기화
    deq = deque()
    
    # TODO: 그래프 구성 및 진입 차수 계산
    in_degree = [0]*vertices
    for i, j in edges:
        in_degree[j] += 1

    # print(in_degree)

    graph = [[] for _ in range(vertices)]
    for i, j in edges:
        graph[i].append(j)
    # TODO: 진입 차수가 0인 정점들을 큐에 추가
    for i in range(vertices):
        if in_degree[i] == 0:
            deq.append(i)
    
    result = []

    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들의 진입 차수 감소

    while deq:
        # print(deq)
        # print(result)
        out = deq.popleft()
        result.append(out)
        for i in graph[out]: # 진입차수 0인 정점들과 연결된 정점들
            in_degree[i] -= 1 # out과 연결된 정점의 간선 없에기 -> 진입차수 -1해서 낮추기
            if in_degree[i] == 0: # 연결되니 정점 i의 진입차수가 0이면
                deq.append(i) # 큐에 넣기
    return result

# 테스트 케이스
if __name__ == "__main__":
    # 과목 선수과목 예제
    vertices = 4
    edges = [
        (0, 1),  # 0 → 1
        (0, 2),  # 0 → 2
        (1, 3),  # 1 → 3
    ]
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

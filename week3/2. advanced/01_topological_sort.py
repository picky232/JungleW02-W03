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
    graph = {} # 노드 : 연결된 노드(진입하는 위치)
    in_degree = [0]*vertices # 진입차수 수
    result = [] # 정렬 순서
    for i, j in edges:
        if i not in graph:
            graph[i] = []
        if j not in graph:
            graph[j] = []
        graph[i].append(j) # 그래프에 추가
        in_degree[j] += 1 # 진입차수 +1
    
    queue = deque()
    # 진입차수 0인 노드 큐에 in
    for i in range(vertices):
        if in_degree[i] == 0:
            queue.append(i)
    
    while queue:
        out = queue.popleft()
        result.append(out) # 뽑은 값은 결과로
        for i in graph[out]: # 연결된 위치로 이동
            in_degree[i]-=1 # 진입차수 수 -1
            if in_degree[i] == 0: # 진입차수 0이면
                queue.append(i) # 큐에 삽입

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
    # edges = {
    #     (0, 3),
    #     (3, 1),
    #     (2, 1),
    #     (3, 2),
    #     (1, 4)
    # }
    
    print("=== 위상 정렬 ===")
    print("과목 관계:")
    print("  0(기초) → 1(중급) → 3(고급)")
    print("  0(기초) → 2(응용)")
    print()
    
    result = topological_sort(vertices, edges)
    print(f"수강 순서: {result}")

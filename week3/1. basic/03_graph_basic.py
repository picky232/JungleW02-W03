"""
[그래프 기본 - 인접 리스트 표현]

문제 설명:
- 그래프를 인접 리스트로 표현합니다.
- 간선(edge)을 추가하고 출력합니다.
- 방향 그래프와 무방향 그래프를 구분합니다.

입력:
- vertices: 정점(vertex) 개수
- edges: 간선 리스트

출력:
- 각 정점에 연결된 정점들

예제:
정점: 4개 (0, 1, 2, 3)
간선: [(0,1), (0,2), (1,2), (2,3)]

무방향 그래프:
0 → [1, 2]
1 → [0, 2]
2 → [0, 1, 3]
3 → [2]

힌트:
- 딕셔너리 사용: {정점: [연결된 정점들]}
- 무방향 그래프는 양방향 추가
"""

def create_graph(vertices, edges, directed=False):
    """
    그래프 생성 (인접 리스트)
    
    Args:
        vertices: 정점 개수
        edges: (출발, 도착) 간선 리스트
        directed: 방향 그래프 여부
    
    Returns:
        그래프 딕셔너리
    """
    # TODO: 빈 그래프 초기화
    graph = {}

    # TODO: 간선 추가
    ## 간선 추가 (u에서 v로)
    ## 무방향 그래프면 반대 방향도 추가
    if not directed:
        for i, j in edges:
            if i not in graph:
                graph.update({i:[]})
            if j not in graph:
                graph.update({j:[]})
            graph[i].append(j)
            graph[j].append(i)
    else:
        for i,j in edges:
            if i not in graph:
                graph.update({i:[]})
            if j not in graph:
                graph.update({j:[]})
            graph[i].append(j)
    return graph

# 테스트 케이스
if __name__ == "__main__":
    # 테스트 케이스 1: 무방향 그래프
    vertices = 4
    edges = [(0, 1), (0, 2), (1, 2), (2, 3)]
    
    print("=== 무방향 그래프 ===")
    graph = create_graph(vertices, edges, directed=False)
    for vertex, neighbors in graph.items():
        print(f"{vertex} → {neighbors}")
    print()
    
    # 테스트 케이스 2: 방향 그래프
    print("=== 방향 그래프 ===")
    graph_directed = create_graph(vertices, edges, directed=True)
    for vertex, neighbors in graph_directed.items():
        print(f"{vertex} → {neighbors}")



"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS: [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

def bfs(graph, start):
    """
    너비 우선 탐색
    
    Args:
        graph: 그래프 딕셔너리
        start: 시작 정점
    
    Returns:
        방문 순서 리스트
    """
    visited = [start] # 시작값 넣기
    
    # TODO: 큐 생성 및 시작 정점 추가
    ## 방문한 정점 집합
    que = deque([start])
    # print(que)

    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가
    k=0
    while que:
        # print("que: ",que)
        # print("visitied: ",visited)
        out = que.popleft() # que에서 노드
        # print(out)
        for i in graph[out]: # 인접노드 탐색
            if i not in visited: # 방문안했으면
                visited.append(i) # 방문에 추가
                que.append(i) # 큐에도 추가
    return visited

# 테스트 케이스
if __name__ == "__main__":
    # 그래프 생성
    graph = {
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}")


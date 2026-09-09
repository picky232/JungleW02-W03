"""
[그래프 - 다익스트라 최단경로 (Dijkstra's Shortest Path)]

▣ 문제 배경
- 가중치가 음이 아닌(0 이상) 방향 그래프에서, 한 출발점 'start' 에서 다른 모든 정점까지의
  최단 거리를 구하는 표준 알고리즘입니다.
- 1959년 Edsger W. Dijkstra 가 발표하였으며, 우선순위 큐(min-heap) 와 결합한 구현은
  공지된 표준 기법입니다. 본 지문과 테스트 케이스는 본 학습 자료를 위해
  자체적으로 작성되었습니다.
- 본 학습에서는 `week2/2. advanced/03_priority_queue` 에서 다룬 힙 자료구조를 활용합니다.

▣ 작은 예시
    정점: 0, 1, 2, 3, 4
    방향 간선(u, v, w):
        0 -> 1 (4)
        0 -> 2 (1)
        2 -> 1 (2)
        2 -> 3 (5)
        1 -> 3 (1)
        3 -> 4 (3)

    그림:
              4
        0 --------> 1
        |\         ^|
        | \1     2/ |
        |  \    /   |1
        |   v  /    v
        |    2 ---> 3 ---> 4
        |    5      3

    start = 0 일 때 최단 거리:
        0 -> 0 : 0
        0 -> 1 : 3   (0->2->1: 1+2)
        0 -> 2 : 1
        0 -> 3 : 4   (0->2->1->3: 1+2+1)
        0 -> 4 : 7   (0->2->1->3->4: 1+2+1+3)

▣ 구현할 함수
dijkstra(n: int, edges: list[tuple[int, int, int]], start: int) -> list
  - 정점은 0, 1, ..., n-1 의 정수로 식별됩니다.
  - edges 는 (u, v, w) 형식의 방향 간선들의 리스트 (w >= 0).
  - 반환값은 길이 n 의 리스트 dist 로,
        dist[i] = start 에서 정점 i 까지의 최단 거리,
        도달 불가능하면 float('inf').
  - dist[start] 는 항상 0 이어야 합니다.

▣ 제약
- 0 <= n <= 1000, 간선 수 <= 5000 정도면 충분.
- 0 <= w <= 10000

▣ 힌트 (heapq 사용, O((V+E) log V))
  import heapq
  - dist 를 INF 로 초기화하고 dist[start] = 0
  - 우선순위 큐에 (0, start) 를 push
  - 큐가 빌 때까지:
      (d, u) = heappop
      if d > dist[u]: continue     # 이미 더 짧은 경로로 처리됨
      for v, w in graph[u]:
          if dist[u] + w < dist[v]:
              dist[v] = dist[u] + w
              heappush(pq, (dist[v], v))
"""

import heapq


INF = float('inf')


def dijkstra(n: int, edges: list, start: int) -> list:
    """
    n: 정점 수 (정점 번호 0 ~ n-1)
    edges: (u, v, w) 형식 방향 간선 리스트
    start: 출발 정점
    반환: 길이 n 의 거리 리스트 (도달 불가 = float('inf'))
    """
    graph = {}
    for i in range(n):
        graph[i] = []
    for u,v,w in edges: # u랑 이어진 노드 v, 둘사이의 거리 w graph의 u안에 저장
        graph[u].append((v,w))
    dist = [float('inf')]*n # 최단 거리 담을 리스트 생성
    # 거리 리스트의 초기값을 inf로 터무니 없이 큰값으로 설정
    dist[start] = 0 # 시작값 초기화
    queue = [(0, start)] # 거리, 시작 값
    while queue:
        d, u = heapq.heappop(queue) # 거리, 현재 정점 값 - 최소힙에 담긴 값중 가중치가 가장 작은거 부터 불러옴
        # d:거리 보다 현재 u까지의 거리가 더 작으면
        # 최선의 선택임으로 다시 돌아감
        if dist[u] < d: # 큐에서 새로 가져온 거리, 현재 위치 값이 이전 정보인지 확인
            continue # 이전 정보라면 다시 되돌아감
        for v, w in graph[u]: # 연결된 원소, 가중치
            if dist[u]+w < dist[v]: # 연결된 원소의 자리까지 가중치 + 가중치
                dist[v] = dist[u] + w # 연결된 원소의 가중치 = 현재 원소 가중치 + 다음 연결된 원소까지의 가중치
                heapq.heappush(queue, (dist[v], v)) # 최소 힙에 푸쉬
    return dist

def _format(dist):
    """출력 표기를 위한 헬퍼: float('inf') 는 'INF' 로 보여줌"""
    return [('INF' if x == INF else x) for x in dist]


if __name__ == "__main__":
    print("[테스트 1] 예시 그래프 (5개 정점)")
    n = 5
    edges = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (2, 3, 5),
        (1, 3, 1),
        (3, 4, 3),
    ]
    print(f"  n={n}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 2] 정점 1개")
    print(f"  n=1, edges=[], start=0")
    print(f"  최단 거리: {_format(dijkstra(1, [], 0))}")
    print()

    print("[테스트 3] 도달 불가능한 정점 포함")
    n = 4
    edges = [(0, 1, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 4] 동일한 거리의 두 경로 (둘 다 7)")
    n = 4
    edges = [(0, 1, 3), (1, 3, 4), (0, 2, 5), (2, 3, 2)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")
    print()

    print("[테스트 5] 0 가중치 간선 포함")
    n = 3
    edges = [(0, 1, 0), (1, 2, 0), (0, 2, 5)]
    print(f"  n={n}, edges={edges}, start=0")
    print(f"  최단 거리: {_format(dijkstra(n, edges, 0))}")

"""
[연결 리스트 - Linked List 기본 구현]

문제 설명:
- 단순 연결 리스트(Singly Linked List)를 구현합니다.
- 노드는 값(data)과 다음 노드를 가리키는 포인터(next)를 가집니다.

입력:
- 연결 리스트에 추가할 값들

출력:
- 연결 리스트의 모든 값 출력

예제:
입력: 1 -> 2 -> 3
출력: [1, 2, 3]


===============================================================
📚 개념 정리: 연결 리스트는 "포인터로 연결된 칸들"
===============================================================

배열(파이썬의 list)과 비교해 보면 차이가 분명합니다.

▶ 배열 [10, 20, 30] 의 메모리 구조 (연속된 칸)

  주소:   1000 1004 1008
        ┌────┬────┬────┐
        │ 10 │ 20 │ 30 │
        └────┴────┴────┘
  → 칸 번호(index) 로 바로 접근, 단 "중간 삽입" 은 뒤를 다 밀어야 함.

▶ 연결 리스트 1 -> 2 -> 3 의 메모리 구조 (떨어진 칸 + 화살표)

  head ─┐
        ▼
       ┌────┬─────┐    ┌────┬─────┐    ┌────┬──────┐
       │ 1  │ ●───┼───▶│ 2  │ ●───┼───▶│ 3  │ None │
       └────┴─────┘    └────┴─────┘    └────┴──────┘
        Node            Node            Node (마지막)

  핵심:
    • head    = "첫 노드를 가리키는 변수" (리스트 손잡이)
    • node.next = "다음 노드를 가리키는 화살표" (포인터/참조)
    • 마지막 노드의 next 는 항상 None (= "이게 끝이야" 표시)
    • 빈 리스트는 head 자체가 None


===============================================================
🔍 자주 나오는 질문 (FAQ)
===============================================================

Q1. Node 만들 때 왜 self.next = None 으로 시작하나요?
    → 새로 만든 노드는 아직 어디에도 "연결" 되어 있지 않습니다.
      "다음이 없다(None)" 로 두고, 나중에 누군가 연결해 줍니다.

Q2. 마지막 노드는 어떻게 알아내나요?
    → next 가 None 인 노드가 곧 마지막 노드입니다.
      그래서 "current.next 가 None 이 될 때까지" 따라가면
      자연스럽게 마지막에 도착합니다.

Q3. current = current.next 는 뭐가 일어나는 건가요?
    → 화살표를 한 칸 따라가는 동작입니다. 그림으로 보면:

      Step 0:  current ──▶ [1|●]──▶[2|●]──▶[3|None]
      Step 1 (current = current.next):
                              current ──▶ [2|●]──▶[3|None]
      Step 2 (current = current.next):
                                            current ──▶ [3|None]
      Step 3 (current = current.next):
                                                          current = None  ← 종료

Q4. 그냥 파이썬 list 쓰면 안 되나요?
    → 됩니다 :) 다만 연결 리스트는 "삽입/삭제가 잦은 곳" (스택/큐/그래프 등)
      에서 더 유리합니다. 자료구조를 직접 구현해 보는 학습용 문제예요.


===============================================================
🛠 풀이 가이드 (Level 별)
===============================================================

append(data) 가 해야 할 일:
  Level 1) 리스트가 비어 있으면 (head 가 None) head 에 새 노드를 꽂는다.
  Level 2) 아니면 head 부터 시작해 "마지막 노드" 까지 이동.
  Level 3) 마지막 노드의 next 에 새 노드를 붙인다.

print_list() 가 해야 할 일:
  Level 1) current 를 head 에서 시작.
  Level 2) current 가 None 이 될 때까지 반복하면서
            values 리스트에 current.data 를 추가하고
            current 를 current.next 로 이동.
"""

class Node:
    """
    연결 리스트의 노드 (한 칸 = 데이터 + 다음 화살표)

        ┌──────┬──────┐
        │ data │ next │ ──▶ (다른 Node 또는 None)
        └──────┴──────┘
    """
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    단순 연결 리스트 (Singly Linked List)

        head ──▶ [data|next] ──▶ [data|next] ──▶ ... ──▶ [data|None]
    """
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        리스트 끝에 노드 추가

        그림으로 보는 두 가지 경우:

        ① 비어 있을 때 (self.head is None)
              head ─▶ None     ──append(7)──▶    head ─▶ [7|None]

        ② 이미 노드가 있을 때
              head ─▶ [1|●]─▶[2|None]
                                       ──append(7)──▶
              head ─▶ [1|●]─▶[2|●]─▶[7|None]
        """
        new_node = Node(data)

        # ─── Level 1: 리스트가 비어 있는 경우 ────────────────────────
        # 힌트: self.head 가 None 이면, head 에 new_node 를 바로 꽂고 return.
        # TODO: 아래 pass 를 지우고 if 문을 완성하세요.
        #   if self.head is None:
        #       self.head = new_node
        #       return
        if self.head == None:
            self.head = new_node
            return

        # ─── Level 2: 마지막 노드 찾기 ──────────────────────────────
        # head 부터 시작해서 next 가 None 이 될 때까지 따라갑니다.
        # 즉 "current.next 가 있는 동안" 계속 이동.
        current = self.head
        # TODO: while 문으로 current 를 마지막 노드까지 이동시키세요.
        #   while current.next is not None:
        #       current = current.next
        while current.next is not None: # node의 포인터가 없는 곳까지 확인 즉 마지막 노드
            current = current.next

        # ─── Level 3: 마지막 노드의 next 에 새 노드를 붙이기 ─────────
        # 위 반복문이 끝나면 current 가 곧 마지막 노드입니다.
        # TODO: current.next = new_node
        current.next = new_node


    def print_list(self):
        """
        리스트의 모든 값을 앞에서부터 차례로 모아 반환합니다.

        예: head ─▶ [10|●]─▶[20|●]─▶[30|None]  →  [10, 20, 30]
        """
        values = []

        # ─── Level 1: 시작 위치 ─────────────────────────────────────
        # current 라는 "이동용 변수" 를 head 에서 시작시킵니다.
        # TODO: current = self.head
        current = self.head

        # ─── Level 2: 끝까지 순회 ──────────────────────────────────
        # current 가 None 이 되면 "리스트의 끝" 이라는 신호입니다.
        # 한 칸 한 칸 따라가면서 data 를 values 에 모으세요.
        # TODO: 아래 두 줄을 while 문 안에 작성하세요.
        #   while current is not None:
        #       values.append(current.data)
        #       current = current.next
        while current is not None: # current가 
            values.append(current.data)
            current = current.next
            
        return values


if __name__ == "__main__":
    print("=== 연결 리스트 테스트 ===")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    result = ll.print_list()
    print(f"리스트: {result}")
    print()

    print("=== 연결 리스트 테스트 2 ===")
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    ll2.append(30)
    ll2.append(40)
    result2 = ll2.print_list()
    print(f"리스트: {result2}")

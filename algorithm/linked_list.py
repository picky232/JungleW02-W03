# 단순 연결리스트
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

# 연결된 리스트
class Linkedlist:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def clear(self):
        self.head = None
    
    def size(self):
        node = self.head
        count = 0
        while node != None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedStack"):
        print(msg)
        node = self.head
        while node != None:
            print("data : ",node.data)
            node = node.link
        print("")

    def getNode(self, pos): # pos 위치 Node 반환
        if pos < 0: return None
        node = self.head
        while pos>0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self, pos): # pos 위치 Node의 데이터 반환
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data

    def replace(self, pos, elem): # pos위치 Node 데이터 변경
        node = self.getNode(pos)
        if node != None:
            node.data = elem

    def find(self, data): # data의 노드 반환
        node = self.head
        while node is not None:
            if node.data == data:
                return node
            node = node.link
        return None

    def insert(self, pos, elem): # 삽입 연산
        before = self.getNode(pos-1) # 삽입할 노드 바로전 위치
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node

    def delete(self, pos): # 삭제 연산
        before = self.getNode(pos-1) # pos위치 바로 이전노드
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

class CircleLinkedQueue: # 원형 연결리스트 응용 - 연결된 큐, 앞,뒤로만 삽입 삭제 가능
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None

    def clear(self):
        self.tail = None

    def enque(self, elem):
        node = Node(elem)
        if self.isEmpty()==None:
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link # 시작 노드 주소랑 연결
            self.tail.link = node
            self.tail = node

    def deque(self):
        if self.isEmpty() != None:
            data = self.tail.link.data
            if self.tail.link == self.tail: # 노드가 하나
                self.tail = None
            else:
                self.tail.link = self.tail.link.link # 맨앞 다음꺼
            return data

class DNode:
    def __init__(self, elem):
        self.data = elem
        self.prev = None
        self.next = None

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def findNode(self, pos):
        node = self.head
        print("head",node.data)
        idx = 0
        while idx!=pos:
            idx+=1
            node = node.next
            print("idx:", idx)
            print(node.data)
        return node # 값이 elem인 노드

    def push(self, elem): # 마지막에 노드 삽입
        node = DNode(elem)
        if self.isEmpty(): # 아무것도 없을때
            self.head = node
            self.tail = node
        else: # 값이 있을때
            node.prev = self.tail # 노드의 prev를 추가전 tail에 연결
            self.tail.next = node # tail의 next를 node로 연결
            self.tail = node # tail 변경

    def display(self, msg="LinkedList"):
        print(msg)
        node = self.head
        while node != None:
            print("data : ",node.data)
            node = node.next
        print("")

    def insert(self, elem, pos):
        node = DNode(elem) # 노드 생성
        if self.isEmpty(): # 연결리스트가 비었을경우
            self.head = node
            self.tail = node
            return
        gijon_node = self.findNode(pos) # pos위치 노드

        node.next = gijon_node.next # 새 노드 next 연결
        node.prev = gijon_node # 새 노드 prev 연결
            
        if gijon_node.next == None: # 기존노드가 맨끝 노드 일때
            self.tail = node # tail 변경
        else: # 증간 노드일때
            gijon_node.next.prev = node # 기존 노드의 다음노드의 prev
        gijon_node.next = node # 기존 노드의 next를 node로 변경

    def delete(self, pos): # 삭제
        if self.isEmpty():
            return None
        node = self.findNode(pos)
        print(node.data)
        # 첫번째 노드
        if node.prev == None:
            self.head = node.next # 링크드 리스트의 헤드 다음노드로 변경
            if self.head != None: # 변경한 head가 None이 아니면
                self.head.prev = None # 변경한 head의 prev None 변경
            else: # 헤드노드만 있었는데 지워서 노드가 없을때
                self.tail = None
        # 마지막 노드
        elif node.next == None:
            self.tail = node.prev
            self.tail.next = None
        # 중간 노드
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        return node.data


s = DLinkedList()
s.display("양방향 연결리스트로 구현한 리스트(초기상태):")
s.push(10)
s.push(20)
s.push(30)
s.push(40)
s.push(50)
s.display("삽입 5개")

s.insert(10, 2)
s.display("insert")
print(s.delete(0))
print(s.delete(1))
s.display("0 [10], 1 [30] 삭제")
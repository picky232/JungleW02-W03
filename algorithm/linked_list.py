# 단순 연결리스트
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

# 연결된 스택 - 단순 연결 리스트 응용
class LinkedStack:
    def __init__(self):
        self.top = None # 시작노드를 가리키는 포인터

    def isEmpty(self): # 공백 상태 검사
        return self.top == None

    def clear(self): # 스택 초기화
        self.top = None

    def push(self, item): # 연결된 스택의 삽입연산
        n = Node(item, self.top) # Step1
        self.top = n  # step3

    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data

    def peak(self):
        if not self.isEmpty():
            return self.top.data

    def size(self):
        node = self.top
        count = 0
        while node != None:
            node = node.link
            count += 1
        return count

    def display(self, msg="LinkedStack"):
        print(msg)
        node = self.top
        while node != None:
            print("data : ",node.data)
            node = node.link
        print("")

odd = LinkedStack()
even = LinkedStack()

for i in range(1, 11, 2):
    odd.push(i)

print(odd.size())
print()
print(odd.display())
print()
print(odd.pop())
print()
print(odd.peak())
print()
print(odd.isEmpty())
print(odd.clear())
print(odd.isEmpty())
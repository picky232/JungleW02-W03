class stack:
    def __init__(self): # 생성자
        self.data = []
        self.pointer = 0

    def push(self, value): # push 데이터 삽입 기능
        self.data.append(value)
        self.pointer += 1

    def pop(self): # pop 맨위 데이터 추출
        pop_data = self.data[self.pointer-1]
        del self.data[self.pointer-1]
        self.pointer-=1
        return pop_data

    def show(self): # 스택안 확인
        print(self.data)

    def empty(self): # 스택 모두 비우기
        for i in range(self.pointer):
            self.data.pop()

    def peek(self):
        print(self.data[-1])


stack1 = stack()
stack1.show()
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.show()

stack1.pop()
stack1.show()

stack1.peek()
stack1.show()

stack1.empty()
stack1.show()


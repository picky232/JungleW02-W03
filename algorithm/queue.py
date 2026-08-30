class queue:
    def __init__(self):
        self.data = []
        self.front = 0 # 추출할 데이터 위치
        self.rear = 0 # 삽입이 일어나는 위치

    def enqueue(self, value): # 원소 삽입
        self.data.append(value)
        self.rear += 1 # 삽입 위치 증가

    def dequeue(self): # 원소 추출
        out_data = self.data[self.front] # 추출한 데이터
        self.front += 1 # 추출할 위치 증가
        return out_data

    def isEmpty(self): # 비엇는지 확인
        return bool(self.data) # 확인후 bool 연산자 반환

    def peak(self): # 맨앞 값 반환
        return self.data[self.front]

    def clear(self): # 큐 초기화
        self.data = []
        self.front = 0
        self.rear = 0

    def show(self): # 큐 보여주기 - f~r까지 
        for i in range(self.front, self.rear):
            print(self.data[i], end=" ")
        print()


q1 = queue()

print(q1.isEmpty())

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.show()

print(q1.dequeue())
q1.show()
print(q1.front, q1.rear)

print(q1.peak())

q1.clear()
q1.show()
class queue:
    def __init__(self):
        self.data = []
        self.front = 0 # 추출할 데이터 위치
        self.rear = 0 # 삽입이 일어나는 위치

    def enqueue(self, value):
        self.data.append(value)
        self.rear += 1

    def dequeue(self):
        out_data = self.data[self.front]
        self.front += 1
        return out_data

    def isEmpty(self):
        return bool(self.data)

    def peak(self):
        return self.data[self.front]

    def clear(self):
        self.data = []
        self.front = 0
        self.rear = 0

    def show(self):
        for i in range(self.front, self.rear):
            print(self.data[i], end=" ")


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
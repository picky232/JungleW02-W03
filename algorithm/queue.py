class queue:
    def __init__(self):
        self.data = []
        self.front = 0 # 추출할 데이터 위치
        self.rear = 0 # 삽입이 일어나는 위치

    def enqueue(self, value):
        self.data.append(value)
        rear += 1

    def dequeue(self):
        out_data = self.data[self.front]
        front += 1
        return out_data

    def isEmpty(self):
        return bool(self.data)

    def peak(self):
        return self.data[self.front]

    def clear(self):
        self.data = []
        self.front = 0
        self.rear = 0
        
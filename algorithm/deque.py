class circledeque:
    def __init__(self, capacity):
        self.data = [None]* capacity
        self.front = 0 # 맨앞 데이터 위치
        self.rear = 0 # 맨뒤 데이터 삽입 위치
        self.size = 0 # 데이터 개수

    # 맨뒤 삽입
    def enqueue(self, value):
        self.data[self.rear] = value
        self.rear = (self.rear+1)%len(self.data)
        self.size += 1

    # 맨앞 삽입
    # Python에서는 음수를 % 연산하면 결과가 나머지의 기준인 
    # 오른쪽 피연산자에 맞춰 양수가 될 수 있음
    def frontAdd(self, value):
        self.front = (self.front-1)%len(self.data) 
        # (0-1) % 5 = 4
        self.data[self.front] = value
        self.size += 1

    # 맨앞 추출
    def dequeue(self):
        out = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front+1)%len(self.data)
        self.size-=1
        print("out", out)

    # 맨뒤 추출
    def rearOut(self):
        out = self.data[self.rear-1]
        self.data[self.rear-1] = None
        self.rear = (self.rear-1)%len(self.data)
        self.size-=1
        print("out", out) 

    # 맨뒤 반환 - 추출x
    def getRear(self):
        print(self.data[self.rear-1])

    # 맨앞 반환 - 추출x
    def getfront(self):
        print(self.data[self.front])

    # front~rear까지 보여주기 - 빈값은 안보여줌
    def show(self):
        out = []
        if self.front < self.rear:
            # 앞 데이터 인덱스 : 뒤 데이터 인덱스+1
            out = self.data[self.front:self.rear] 
        else: # front >= rear
            # 앞 데이터 인덱스 : 데이터 길이
            f_l = self.data[self.front:len(self.data)] 
            # 처음 : 마지막 데이터
            r_l = self.data[0:self.rear]
            out = f_l + r_l
        print(f"front: {self.front} rear: {self.rear} \n데이터 수: {self.size} | 데이터 출력결과: {out}")
        print("실제 배열안", self.data)

cd1 = circledeque(5)
cd1.show()
# front: 0 rear: 0 
# 데이터 수: 0 | 데이터 출력결과: [None, None, None, None, None]
# 실제 배열안 [None, None, None, None, None]

# 짝수는 뒤로 삽입, 홀수는 앞으로 삽입
for i in range(6):
    if i%2==0:
        cd1.enqueue(i)
    else:
        cd1.frontAdd(i)
cd1.show()
# front: 3 rear: 3 
# 데이터 수: 5 | 데이터 출력결과: [3, 1, 0, 2, 4]
# 실제 배열안 [0, 2, 4, 3, 1]

print("맨앞")
cd1.dequeue()
# 맨앞
# out 3
print("맨뒤")
cd1.rearOut()
# 맨뒤
# out 4
cd1.show()
# front: 4 rear: 2 
# 데이터 수: 3 | 데이터 출력결과: [1, 0, 2]
# 실제 배열안 [0, 2, None, None, 1]
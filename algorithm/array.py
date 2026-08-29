# 배열 구현하기
# 객체에서 self는 자기자신을 말함
class Array:
    def __init__(self, capacity): # capacity 용량
        self.data = [None] * capacity
        self.size = 0 # 배열에 들어있는원소 개수 기록, 다음 공간 가리키는 포인터
        self.capacity = capacity # 용량

    # 맨뒤에 추가
    def append(self, value):
        # 배열 원소개수가 용량이랑 같으면 배열용량 늘리기
        if self.size == self.capacity:
            self.data += [None]
            self.capacity += 1
        self.data[self.size] = value
        self.size += 1

    # 인덱스 위치 데이터 조회
    def get(self, index):
        # 인덱스 범위가 0보다 작거나 크면 에러 출력
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        return self.data[index]

    # 인덱스 위치의 데이터 제거
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        self.data[index] = None # 인덱스위치 데이터 삭제
        for idx in range(index+1, self.size): # 지울인덱스 다음인덱스위치, 끝 원소위치
            move_data = self.data[idx] # 옮길 데이터 담기
            self.data[idx-1] = move_data
        self.data[self.size-1] = None
        self.size -= 1 # 포인터 위치 변경, 배열 개수 감소

    # 마지막 값 삭제
    def pop(self):
        pop_data = self.data[self.size-1]
        self.data[self.size-1] = None
        self.size -= 1
        return pop_data

    # 현재 원소 개수 반환 - 배열크기 말하는게 아님
    # arr1.len() => len(arr1) 가능하도록 구현
    def __len__(self):
        return self.size

    # 중간 삽입
    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        
        if self.size == len(self.data):
            self.data += [None]
            self.capacity += 1 # 용량 추가
        # 이게 문제인 이유 len(self.data)는 내가 만든 메소드를 사용하는게 아닌 객체내 정의된 배열의 크기를 파이썬 내장함수로 셈
        # for idx in range(len(self.data)-1, index, -1):
        for idx in range(self.size, index, -1): # 다음 삽입 위치, 중간삽입할 인덱스
            move_data = self.data[idx-1] # 옮길 데이터 저장
            self.data[idx] = move_data # 한칸씩 뒤에 데이터 저장
        self.data[index] = value
        self.size += 1 # 데이터 추가후 포인터 이동

    def clear(self):
        for i in range(self.size):
            self.data[i] = None
        self.size = 0


arr1 = Array(5)
print("append", [10,20,30,40])
arr1.append(10)
arr1.append(20)
arr1.append(30)
arr1.append(40)
print("after append", arr1.data)

arr1.insert(2, '중간삽입')
print("insert", arr1.data)

print("pop",arr1.pop())
print(arr1.data)

arr1.remove(1)
print("remove", 1)
print(arr1.data)

print("len", len(arr1))

print("get", arr1.get(1))
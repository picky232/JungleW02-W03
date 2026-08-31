def isValidPos(x, y): # x,y가 갈 수 있는 방인지 검사하는 함수
    if x<0 or y<0 or x >= MAZE_COL or y >= MAZE_ROW:
        return False
    return mapping[y][x] == '0' or mapping[y][x] == 'x' # x,y가 0이거나 x 즉 벽으로 막혀있지 않으면 True 막혀있으면 False


def DFS(x, y): # 시작위치
    stack = []
    stack.append((x, y)) # stack 안에 좌표 쌓기
    print("DFS: ")

    while stack: # 스택에 값이 있으면
        here = stack.pop() # stack맨 앞 값하나 추출
        print(here, end='->')
        (x,y) = here # 열, 행
        if mapping[y][x] == 'x': # 꺼낸 위치가 도착지이면 종료
            return True
        else:
            mapping[y][x]='.' # 파이썬은 [행], [열] 순으로 써야함, 확인한 위치
            if isValidPos(x,y-1): stack.append((x,y-1)) # 상
            if isValidPos(x,y+1): stack.append((x,y+1)) # 하
            if isValidPos(x+1,y): stack.append((x+1,y)) # 좌
            if isValidPos(x-1,y): stack.append((x-1,y)) # 우
        print('현재스택', stack)
    return False

mapping = [
    ['1','1','1','1','1','1'],
    ['e','0','0','0','0','1'],
    ['1','0','1','0','1','1'],
    ['1','1','1','0','0','x'],
    ['1','1','1','0','1','1'],
    ['1','1','1','1','1','1']
]
MAZE_ROW = len(mapping)
MAZE_COL = len(mapping[0])

result = DFS(1, 0)
if result:
    print("미로탐색 성공")
else:
    print("미로탐색 실패")

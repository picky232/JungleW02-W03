def isValidPos(x, y): # x,y가 갈 수 있는 방인지 검사하는 함수
    if x<0 or y<0 or x >= MAZE_COL or y >= MAZE_ROW:
        return False
    return mapping[y][x] == '0' or mapping[y][x] == 'x'


def DFS(x, y): # 시작위치
    stack = []
    stack.append((x, y))
    print("DFS: ")

    while stack:
        here = stack.pop()
        print(here, end='->')
        (x,y) = here # 열, 행
        if mapping[y][x] == 'x':
            return True
        else:
            mapping[y][x]='.' # 파이썬은 [행], [열] 순으로 써야함
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

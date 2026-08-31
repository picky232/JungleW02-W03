from myqueue import queue

def isValidPos(x, y): # x,y가 갈 수 있는 방인지 검사하는 함수
    if x<0 or y<0 or x >= MAZE_COL or y >= MAZE_ROW:
        return False
    return mapping[y][x] == '0' or mapping[y][x] == 'x' # x,y가 0이거나 x 즉 이동가능한 위치라면 True 아니면 False

def BFS(x, y):
    que = queue()
    que.enqueue((x,y))
    print("BFS: ")

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end="->")
        x,y = here
        if(mapping[y][x]=='x'): 
            return True
        else:
            mapping[y][x] = '.'
            if isValidPos(x, y-1): # 상
                que.enqueue((x, y-1))
            if isValidPos(x, y+1): # 하
                que.enqueue((x, y+1))
            if isValidPos(x-1, y): # 좌
                que.enqueue((x-1, y))
            if isValidPos(x+1, y): # 우
                que.enqueue((x+1, y))
    return False

mapping = [
    ['1','1','1','1','1','1'],
    ['e','0','1','0','0','1'],
    ['1','0','0','0','1','1'],
    ['1','0','1','0','1','1'],
    ['1','0','1','0','0','x'],
    ['1','1','1','1','1','1']
]

MAZE_ROW = len(mapping)
MAZE_COL = len(mapping[0])

result = BFS(0, 1) # 열,행 -> 우리가 좌표평면할때 열,행으로 씀
if result: print("탐색성공")
else: print("탐색실패")
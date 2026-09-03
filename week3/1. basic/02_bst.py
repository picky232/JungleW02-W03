"""
[이진 검색 트리 - Binary Search Tree (BST)]

문제 설명:
- 이진 검색 트리에서 값을 검색합니다.
- BST 특징: 왼쪽 자식 < 부모 < 오른쪽 자식
- 이 특성을 이용하여 빠른 검색이 가능합니다.
- 왼쪽 서브트리의 모든 값 < 현재 노드 값
- 오른쪽 서브트리의 모든 값 > 현재 노드 값

입력:
- root: 트리의 루트 노드
- target: 찾을 값

출력:
- True: 값이 존재
- False: 값이 없음

예제:
트리:
      5
     / \
    3   7
   / \
  2   4

찾는 값: 4 → True
찾는 값: 6 → False

힌트:
- target < root.value → 왼쪽으로 이동
- target > root.value → 오른쪽으로 이동
- target == root.value → 찾음!
"""

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def search_bst(root, target):
    """
    BST에서 값 검색
    
    Args:
        root: 트리 루트
        target: 찾을 값
    
    Returns:
        True/False
    """
    # TODO: root가 None이면 False 반환
    if root == None:
        return False
    # print(root.value)
    # TODO: 값을 찾으면 True 반환
    ## target이 작으면 왼쪽 서브트리에서 검색
    ## target이 크면 오른쪽 서브트리에서 검색
    if root.value == target:
        return True
    if root.value > target:
        return search_bst(root.left, target)
    if root.value < target:
        return search_bst(root.right, target)
    
    

# 테스트 케이스
if __name__ == "__main__":
    # BST 생성:
    #       5
    #      / \
    #     3   7
    #    / \
    #   2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print("=== 이진 검색 트리 ===")
    print("트리 구조: 5를 루트로 하는 BST")
    
    test_values = [2, 4, 5, 6, 7]
    for val in test_values:
        result = search_bst(root, val)
        print(f"값 {val} 검색: {result}")



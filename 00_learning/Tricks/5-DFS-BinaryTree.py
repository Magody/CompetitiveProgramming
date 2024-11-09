
# data structure
class Node:
    def __init__(self, data, node_left=None, node_right=None) -> None:
        self.data = data
        self.node_left = node_left
        self.node_right = node_right
    def set_children(self, node_left, node_right):
        self.node_left = node_left
        self.node_right = node_right




def DFS(tree: Node, level, levels_already_seen, answer):
    # important: levels_already_seen and answer should be passed by reference
    if tree == None:
        return None
    root = tree.data
    
    # Pre-order: Root-Right-Left
    if level not in levels_already_seen:
        levels_already_seen.append(level)
        answer.append(root)
    
    DFS(tree.node_right, level+1, levels_already_seen, answer)
    DFS(tree.node_left, level+1, levels_already_seen, answer)
  
def solve(tree):
    answer_by_reference = []
    DFS(tree, 0, [], answer_by_reference)
    return answer_by_reference

def test():
    # MOCKING THE TREES FOR TEST
    tree1 = Node(1, Node(2), Node(3))
    # set the left side
    tree1.node_left.set_children(Node(4), Node(5))
    tree1.node_left.node_left.node_right = Node(7, Node(8), None)
    # set the right side
    tree1.node_right.set_children(None, Node(6))


    tree2 = Node(1, Node(2), Node(3))
    # set the left side
    tree2.node_left.set_children(Node(6), Node(7))
    tree2.node_left.node_left.set_children(Node(8), Node(9))
    tree2.node_left.node_left.node_left.node_left = Node(10)
    
    # set the right side
    tree2.node_right.set_children(Node(5), Node(4))

    test_cases = [
        tree1,
        tree2
    ]
    expected = [
        [1, 3, 6, 7, 8],
        [1, 3, 4, 9, 10]
    ]
    for i in range(len(test_cases)):
        solution = None
        try:
            solution = solve(test_cases[i])
            assert solution == expected[i]
            print("OK")
        except Exception as error:
            print(f"Error, test {test_cases[i]}, expected {expected[i]}, calculated {solution}", error)

test()
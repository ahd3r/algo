r"""
Given a Binary Tree (BT), convert it to a doubly-linked list (DLL) in-place.
The left and right pointers in nodes are to be used as previous and next
pointers respectively in the converted DLL. The order of nodes in DLL must be same
as the in-order traversal of the given Binary Tree. The first node of the in-order
traversal (left-most node in BT) must be the head node of the DLL.

For example, consider the following tree:

       10
      /   \
     12    15
    /  \   /
   25  30 36

The above tree should be in-place converted to the following list:

head --> 25 <--> 12 <--> 30 <--> 10 <--> 36 <--> 15
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTreeDoublyLinkedList:
    # Implement this class!
    def __init__(self):
        self.head = None # Node
        self.prev = None

    def create_list(self, root):
        if root.left != None:
            self.create_list(root.left)
        if self.head == None:
            self.head = root
            self.prev = root
        else:
            self.prev.right = root
            root.left = self.prev
            self.prev = root
        if root.right != None:
            self.create_list(root.right)

    # def __init__(self):
    #     self.head = None # Node
    #     self.cur = []

    # def traverse(self, root):
    #     if root.left != None:
    #         self.traverse(root.left)
    #     self.cur.append(root)
    #     if root.right != None:
    #         self.traverse(root.right)

    # def create_list(self, root):
    #     self.traverse(root) # [25, 12, 30 , 10, 36, 15]
    #     for c in range(len(self.cur)):
    #         if c == 0:
    #             self.cur[c].left = None
    #             self.cur[c].right = self.cur[c+1]
    #         elif c == len(self.cur) - 1:
    #             self.cur[c].right = None
    #             self.cur[c].left = self.cur[c-1]
    #         else:
    #             self.cur[c].left = self.cur[c-1]
    #             self.cur[c].right = self.cur[c+1]
    #     self.head = self.cur[0]


def print_list(head):
    prev = None
    current = head
    print("Check forward")
    while current is not None:
        print(current.val, end="->")
        prev = current
        current = current.right
    print("\nCheck reverse")
    while prev is not None:
        print(prev.val, end="->")
        prev = prev.left


# Test case
def test_solution() -> None:
    node1 = Node(10)
    node2 = Node(12)
    node3 = Node(25)
    node4 = Node(30)
    node5 = Node(15)
    node6 = Node(36)

    node1.left = node2
    node2.left = node3
    node2.right = node4
    node1.right = node5
    node5.left = node6

    dll = BinaryTreeDoublyLinkedList()
    dll.create_list(node1)

    print_list(dll.head)

test_solution()

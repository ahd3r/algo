class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def toList(self):
        leftList = []
        rightList = []
        if self.left:
            leftList = self.left.toList()
        if self.right:
            rightList = self.right.toList()
        return leftList + [self.value] + rightList

    def applyBalancedTree(self, list):
        self.left = None
        self.right = None
        self.value = None
        if len(list) == 0:
            return self
        value = list[len(list) // 2]
        self.value = value
        leftList = list[:len(list) // 2]
        rightList = list[(len(list) // 2) + 1:]
        curRightRoot = self
        while value in leftList or value in rightList:
            if value in leftList:
                curRightRoot.right = BST(value)
                curRightRoot = curRightRoot.right
                leftListIndex = leftList.index(value)
                leftList = leftList[:leftListIndex] + \
                    leftList[leftListIndex+1:]
            if value in rightList:
                curRightRoot.right = BST(value)
                curRightRoot = curRightRoot.right
                rightListIndex = rightList.index(value)
                rightList = rightList[:rightListIndex] + \
                    rightList[rightListIndex+1:]
        if len(leftList) > 0:
            self.left = BST(0)
            self.left.applyBalancedTree(leftList)
        if len(rightList) > 0:
            curRightRoot.right = BST(0)
            curRightRoot.right.applyBalancedTree(rightList)
        return self

    def insert(self, value):
        self.insertWithoutBalance(value)
        tree = self.toList()
        self.applyBalancedTree(tree)
        return self

    def insertWithoutBalance(self, value):
        if value < self.value:
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def removeWithoutBalance(self, value, first=True):
        if self.value == value:
            if first and self.left == None and self.right == None:
                return self
            curLeft = self.left
            curRight = self.right
            if curLeft.right != None:
                while curLeft.right.right:
                    curLeft = curLeft.right
            if curRight.left != None:
                while curRight.left.left:
                    curRight = curRight.left
            leftVal = curLeft.value if not curLeft.right else curLeft.right.value
            rightVal = curRight.value if not curRight.left else curRight.left.value
            if abs(value - leftVal) < abs(value - rightVal):
                self.value = leftVal
                if curLeft.right:
                    curLeft.right = None
                else:
                    self.left = None
            else:
                self.value = rightVal
                if curRight.left:
                    curRight.left = None
                else:
                    self.right = None
        elif value < self.value:
            if self.left != None:
                if self.left.value == value and self.left.left == None and self.left.right == None:
                    self.left = None
                else:
                    self.left.remove(value, False)
        else:
            if self.right != None:
                if self.right.value == value and self.right.left == None and self.right.right == None:
                    self.right = None
                else:
                    self.right.remove(value, False)
        return self

    def contains(self, value):
        if value < self.value:
            if self.left == None:
                return False
            self.left.contains(value)
        elif value > self.value:
            if self.right == None:
                return False
            self.right.contains(value)
        else:
            return True

    def remove(self, value):
        self.removeWithoutBalance(value)
        tree = self.toList()
        self.applyBalancedTree(tree)
        return self

bst = BST(10)
bst.insert(5)
bst.insert(15)
bst.insert(25)
bst.insert(53)
bst.remove(10)
bst.contains(53)

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.len = 0

    def length(self):
        return self.len

    def insertFirst(self, data):
        newNode = ListNode(data)
        newNode.next = self.head
        self.head = newNode
        self.len += 1

    def printList(self):
        curNode=self.head
        while curNode is not None:
            print(curNode.data)
            curNode=curNode.next

L=List()
#for i in range(1, 6, 1):
L.insertFirst(15)
L.insertFirst(23)
L.insertFirst(35)
print("so phan tu hien co trong",L.length())
print("danh sach gom cac phan tu sau:")
L.printList()
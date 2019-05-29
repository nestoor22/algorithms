import gc

class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = DNode(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def add_mid(self, prev_node, new_data):
        pr_node = self.head
        while prev_node > 1:
            pr_node = pr_node.next
            prev_node -= 1
        if pr_node is None:
            return
        new_node = DNode(new_data)
        new_node.next = pr_node.next
        pr_node.next = new_node
        new_node.prev = pr_node

        if new_node.next is not None:
            new_node.next.prev = new_node

    def append(self, new_data):
        new_node = DNode(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last
        return


    def deleteNode(self, delnode):
        if self.head is None or delnode is None:
            return
        if self.head == delnode:
            self.head = delnode.next
        if delnode.next is not None:
            delnode.next.prev = delnode.prev
        if delnode.prev is not None:
            delnode.prev.next = delnode.next
        gc.collect()

    def show(self, node):
        res = '['
        while node is not None:
            res += str(node.data) + ','
            node = node.next
        res += ']'
        print(res)

    def del_beg(self):
        self.deleteNode(self.head)

    def del_end(self):
        if self.head.next is None:
            self.deleteNode(self.head)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        self.deleteNode(node)

    def del_elem(self, elem):
        node = self.head
        if node.data == elem:
            self.deleteNode(node)
            return
        else:
            while node.data != elem:
                node = node.next
                if node is None:
                    print("Елемент відсутній")
                    return
            self.deleteNode(node)

    def del_pos(self, pos):
        if pos == 0:
            self.del_beg()
            return
        node = self.head
        while pos >= 1:
            node = node.next
            pos -= 1
        self.deleteNode(node)
        return

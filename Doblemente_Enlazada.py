class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = DNode(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur

    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=" <-> ")
            cur = cur.next
        print("None")

    def update(self, index, new_data):
        cur = self.head
        count = 0
        while cur:
            if count == index:
                cur.data = new_data
                return
            cur = cur.next
            count += 1

    def delete(self, data):
        cur = self.head
        while cur:
            if cur.data == data:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return
            cur = cur.next

    def delete_at_index(self, index):
        cur = self.head
        count = 0
        while cur:
            if count == index:
                if cur.prev:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next:
                    cur.next.prev = cur.prev
                return
            cur = cur.next
            count += 1

    def search(self, value):
        cur = self.head
        index = 0
        while cur:
            if cur.data == value:
                return index
            cur = cur.next
            index += 1
        return -1

    def sort(self):
        if not self.head:
            return
        changed = True
        while changed:
            changed = False
            cur = self.head
            while cur.next:
                if cur.data > cur.next.data:
                    cur.data, cur.next.data = cur.next.data, cur.data
                    changed = True
                cur = cur.next

print("== Lista Doblemente Enlazada ==")
dll = DoublyLinkedList()
dll.append(3)
dll.append(1)
dll.append(4)
dll.append(2)

print("Lista inicial:")
dll.display()

print("Buscar 4:", dll.search(4))

dll.update(2, 10)
print("Después de actualizar índice 2 a 10:")
dll.display()

dll.delete(1)
print("Después de eliminar el valor 1:")
dll.display()

dll.delete_at_index(0)
print("Después de eliminar el índice 0:")
dll.display()

print("Antes de ordenar:")
dll.display()
dll.sort()
print("Después de ordenar:")
dll.display()

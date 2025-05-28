class CDNode:
    def __init__(self, data):
        self.data = data
        self.prev = self
        self.next = self

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = CDNode(data)
        if not self.head:
            self.head = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def display(self):
        if not self.head:
            print("None")
            return
        cur = self.head
        while True:
            print(cur.data, end=" <-> ")
            cur = cur.next
            if cur == self.head:
                break
        print("(circular)")

    def update(self, index, new_data):
        if not self.head:
            return
        cur = self.head
        count = 0
        while True:
            if count == index:
                cur.data = new_data
                return
            cur = cur.next
            count += 1
            if cur == self.head:
                break

    def delete(self, data):
        if not self.head:
            return
        cur = self.head
        while True:
            if cur.data == data:
                if cur.next == cur:  # solo un nodo
                    self.head = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    if cur == self.head:
                        self.head = cur.next
                return
            cur = cur.next
            if cur == self.head:
                break

    def delete_at_index(self, index):
        if not self.head:
            return
        cur = self.head
        count = 0
        while True:
            if count == index:
                if cur.next == cur:
                    self.head = None
                else:
                    cur.prev.next = cur.next
                    cur.next.prev = cur.prev
                    if cur == self.head:
                        self.head = cur.next
                return
            cur = cur.next
            count += 1
            if cur == self.head:
                break

    def search(self, value):
        if not self.head:
            return -1
        cur = self.head
        index = 0
        while True:
            if cur.data == value:
                return index
            cur = cur.next
            index += 1
            if cur == self.head:
                break
        return -1

    def sort(self):
        if not self.head:
            return
        changed = True
        while changed:
            changed = False
            cur = self.head
            while True:
                next_node = cur.next
                if next_node == self.head:
                    break
                if cur.data > next_node.data:
                    cur.data, next_node.data = next_node.data, cur.data
                    changed = True
                cur = cur.next

print("\n== Lista Circular Doblemente Enlazada ==")
cdll = CircularDoublyLinkedList()
cdll.append(6)
cdll.append(2)
cdll.append(9)
cdll.append(5)

print("Lista inicial:")
cdll.display()

print("Buscar 9:", cdll.search(9))

cdll.update(0, 4)
print("Después de actualizar índice 0 a 4:")
cdll.display()

cdll.delete(2)
print("Después de eliminar el valor 2:")
cdll.display()

cdll.delete_at_index(1)
print("Después de eliminar el índice 1:")
cdll.display()

print("Antes de ordenar:")
cdll.display()
cdll.sort()
print("Después de ordenar:")
cdll.display()

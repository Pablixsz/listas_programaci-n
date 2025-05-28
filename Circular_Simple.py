class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.tail = None

    def append(self, data):
        new_node = CNode(data)
        if not self.tail:
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node

    def display(self):
        if not self.tail:
            print("None")
            return
        cur = self.tail.next
        while True:
            print(cur.data, end=" -> ")
            cur = cur.next
            if cur == self.tail.next:
                break
        print("(circular)")

    def update(self, index, new_data):
        if not self.tail:
            return
        cur = self.tail.next
        count = 0
        while True:
            if count == index:
                cur.data = new_data
                return
            cur = cur.next
            count += 1
            if cur == self.tail.next:
                break

    def delete(self, data):
        if not self.tail:
            return
        prev = self.tail
        cur = self.tail.next
        while True:
            if cur.data == data:
                if cur == self.tail and cur == self.tail.next:
                    self.tail = None
                else:
                    prev.next = cur.next
                    if cur == self.tail:
                        self.tail = prev
                return
            prev, cur = cur, cur.next
            if cur == self.tail.next:
                break

    def delete_at_index(self, index):
        if not self.tail:
            return
        prev = self.tail
        cur = self.tail.next
        count = 0
        while True:
            if count == index:
                if cur == self.tail and cur == self.tail.next:
                    self.tail = None
                else:
                    prev.next = cur.next
                    if cur == self.tail:
                        self.tail = prev
                return
            prev, cur = cur, cur.next
            count += 1
            if cur == self.tail.next:
                break

    def search(self, value):
        if not self.tail:
            return -1
        cur = self.tail.next
        index = 0
        while True:
            if cur.data == value:
                return index
            cur = cur.next
            index += 1
            if cur == self.tail.next:
                break
        return -1

    def sort(self):
        if not self.tail:
            return
        changed = True
        while changed:
            changed = False
            cur = self.tail.next
            while cur.next != self.tail.next:
                next_node = cur.next
                if cur.data > next_node.data:
                    cur.data, next_node.data = next_node.data, cur.data
                    changed = True
                cur = cur.next

print("\n== Lista Circular Simple ==")
cll = CircularLinkedList()
cll.append(7)
cll.append(3)
cll.append(9)
cll.append(1)

print("Lista inicial:")
cll.display()

print("Buscar 9:", cll.search(9))

cll.update(1, 8)
print("Después de actualizar índice 1 a 8:")
cll.display()

cll.delete(3)
print("Después de eliminar el valor 3:")
cll.display()

cll.delete_at_index(0)
print("Después de eliminar el índice 0:")
cll.display()

print("Antes de ordenar:")
cll.display()
cll.sort()
print("Después de ordenar:")
cll.display()

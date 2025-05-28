class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):  # Create
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def display(self):  # Read
        cur = self.head
        while cur:
            print(cur.data, end=" -> ")
            cur = cur.next
        print("None")

    def update(self, index, new_data):  # Update
        cur = self.head
        count = 0
        while cur:
            if count == index:
                cur.data = new_data
                return
            cur = cur.next
            count += 1

    def delete(self, data):  # Delete by value
        cur = self.head
        if cur and cur.data == data:
            self.head = cur.next
            return
        prev = None
        while cur:
            if cur.data == data:
                prev.next = cur.next
                return
            prev = cur
            cur = cur.next

    def delete_at_index(self, index):
        if index == 0 and self.head:
            self.head = self.head.next
            return
        cur = self.head
        prev = None
        count = 0
        while cur:
            if count == index:
                prev.next = cur.next
                return
            prev = cur
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
        if not self.head or not self.head.next:
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

my_list = LinkedList()
my_list.append(5)
my_list.append(2)
my_list.append(1)
my_list.append(8)
my_list.append(5)

print("Lista inicial:")
my_list.display()

index_of_13 = my_list.search(13)
print(f"El valor 13 se encuentra en el índice: {index_of_13}")

my_list.update(1, 8)
print("Lista después de actualizar el índice 1 a 8:")
my_list.display()

my_list.delete(13)
print("Lista después de eliminar el valor 13:")
my_list.display()

my_list.delete_at_index(0)
print("Lista después de eliminar el elemento en el índice 0:")
my_list.display()

print("Lista sin ordenar:")
my_list.display()

my_list.sort()
print("Lista ordenada:")
my_list.display()

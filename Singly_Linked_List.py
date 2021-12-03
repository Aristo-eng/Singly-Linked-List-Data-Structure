class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def print_linked_list(self):
        if self.head is None:
            return ""

        node = self.head
        while node:
            print(node.value, end = "   ")
            node = node.next

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        ref_head = self.head
        while ref_head.next:
            ref_head = ref_head.next
        ref_head.next = new_node 

    




if __name__ == '__main__': 
    # Start with an empty list
    list_s = SingleLinkedList()

    # Insert value at the end.  So linked list becomes value->None
    list_s.insert_at_end(1)
    list_s.insert_at_end(2)


    # print the linked list
    list_s.print_linked_list()

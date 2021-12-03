class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__': 
    # Start with an empty list
    list = SingleLinkedList()
    print(type(list))
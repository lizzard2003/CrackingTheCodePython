# Linked List
# removing duplicates from an unsorted linked list
# singly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_duplicates(self):
        if not self.head:
            return

        unique_values = set()
        current = self.head
        previous = None

        while current:
            if current.data in unique_values:
                # Remove the duplicate node
                previous.next = current.next
            else:
                unique_values.add(current.data)
                previous = current
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage:
if __name__ == "__main__":
    linked_list = LinkedList() # creating a new linked list
    linked_list.append(3) # adding numbers to linked list 
    linked_list.append(1)
    linked_list.append(3)
    linked_list.append(5)
    linked_list.append(1)

    print("Original Linked List:")
    linked_list.display()

    linked_list.remove_duplicates()  # calling the function 

    print("\nLinked List after removing duplicates:")
    linked_list.display()

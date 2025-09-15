class Node:
    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist")

    def add_end(self, name):
        new_node = Node(name)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"{name} added to the end of the waitlist")

    def remove(self, name):
        if not self.head:
            print(f"{name} not found (waitlist empty)")
            return

        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist")
            return

        current = self.head
        while current.next and current.next.name != name:
            current = current.next

        if current.next:
            current.next = current.next.next
            print(f"Removed {name} from the waitlist")
        else:
            print(f"{name} not found")

    def print_list(self):
        if not self.head:
            print("The waitlist is empty")
            return
        print("Current waitlist:")
        current = self.head
        while current:
            print(f"- {current.name}")
            current = current.next
def waitlist_manager():
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)
        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)
        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)
        elif choice == "4":
            waitlist.print_list()
        elif choice == "5":
            print("Exiting waitlist manager.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    waitlist_manager()

#Design Memo
#Custom singly linked lists were implemented into this program in order to manage the event waitlist.
#Each customer gets stored as a Node object and holds their name as well as a reference
#This linklist class provides ways to add customers to the front or back, or remove them altogether, and allows users to print out the list entirely.
#A command-line interface allows support staff to interact with these commands through a simple menu system.
#The head pointer is the mostimportant part of this structure, as it keeps track of the first node in the list.
#All operations begin at the head and follow the chain of next pointers. This means, if a customer is added at the front, they become the head node, and points to the previous head node.
#Removing a customer adjusts the pointers so that the list skips over the removed node, while adding someone to the end walks through the list until it reaches the final node, and attaches the new node there.
#Printing the list traverses from the head to the end, which in turn displays each name in the list.
#Custom lists are useful in the real world when a built-in data structure is too rigid or dated.
#By implementing our own lists, we have full control over how elements are added, removed, or traversed.
#This makes the system more flexible and tailors it to the problems at  hand.
#An engineer might need a list like this, if for example, a ticketing system has to add VIP customers to the front quickly.
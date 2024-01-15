class Node():# almost the same code used for hash table
    def __init__(self,data=None):
            self.data=data
            self.next=None

class linked_list():
    def __init__(self):
            self.head = Node()

    # adding a new node
    def add(self,data):
            new_node = Node(data)
            current = self.head
            while current.next!= None:
                    current = current.next
            current.next = new_node
    # deleting a node
    def delete(self, address):
        if address < self.Len():
            current_index = 0
            current = self.head
            while True:
                past_node = current
                current = current.next
                if current_index == address:# if it found the address:
                    past_node.next = current.next# it will make previous node point
                    # towards the next node after the current node which is deleted
                    # baiscally over writes the node.
                    return
                else:
                    current_index += 1
        else:
            print("the address proivded is out of range")
    # finds address of the given data if data is in list
    def find(self, data):
        current = self.head
        address = 0# will output address of the value if it's in list
        breakloop = False# will be used to stop the loop if needed
        while current.next.data != data and (breakloop == False):
            address += 1
            if address < self.Len():# checks to see if it's on last node
                current = current.next
            else:
                print("data is not in list")
                breakloop = True# breaks the while loop
        if breakloop == False:
            print("data is located in address " + str(address))
        
                

    # finding length of list for deleting function
    def Len(self):
            current = self.head
            length = 0
            while current.next != None:
                    length += 1
                    current = current.next
            return length
        
    def Length(self):
            current = self.head
            length = 0
            while current.next != None:
                    length += 1
                    current = current.next
            print("length is " + str(length))


     
    def view(self):
            List = []
            current = self.head
            while current.next != None:
                    current =current.next
                    List.append(current.data)
            print(List)

l1 = linked_list()
run = True
while run:# allows person who runs code to test the linked list in real time
    Input = str(input("what do you want to do with the linked list"))
    if Input == "add()":
        data = int(input("please enter data to be added"))
        l1.add(data)
    elif Input == "delete()":
        address = int(input("please enter which address to be deleted"))
        l1.delete(address)
    elif Input == "Length()":
        l1.Length()
    elif Input == "view()":
        l1.view()
    elif Input == "find()":
        data = int(input("please enter the data of which you want to find"))
        l1.find(data)
    else:
        pass

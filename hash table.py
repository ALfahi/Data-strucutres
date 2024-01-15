######## code for linked list to hangle collsions######
class Node():# creating a node for the linked list
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class linked_list():# linked list will contain collisions for the hash table
    def __init__(self):
        self.head = Node()

    # adding a new node
    def add(self, key, value):
        new_node = Node(key, value)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        Hash.number += 1# adds one to the number of items in hash table

    # deleting a node
    def delete(self, key):
        current_index = 0
        current = self.head
        while current_index < self.Len() :
            past_node = current
            current = current.next
            if current.key == key:
                past_node.next = current.next
                Hash.number -= 1# subtracts one from hash table 
                return
            else:
                current_index += 1
        print("not in list")


    # finds address of the given data if data is in the list
    def find(self, key):
        current = self.head.next
        address = 0# intialising the address
        while current != None:
            if current.key == key: #if it found the key
                print(current.key + ":", current.value)
                return
            current = current.next# if it didn't find the key then it will go on to the next one
            address += 1# increment address 
        print(f"Key does not exist")# if it goes through the whole linked list and the key was not found

    # finding length of the list for deleting function
    def Len(self):
        current = self.head
        length = 0
        while current.next is not None:
            length += 1
            current = current.next
        return length

    def Length(self):# length used to print out the length of the list
        current = self.head
        length = 0
        while current.next is not None:
            length += 1
            current = current.next
        print("Length is " + str(length))

    def view(self):# used to actually print the linked list
        List = []# appends all items into a list and then prints the list
        current = self.head.next
        while current != None:
            List.append((current.key, current.value))
            current = current.next
        print(List)





################### code for hash table starts here ###########

class hash_table():
    def __init__(self):
        self.length = 9# how many columns in hash table
        self.number = 0# how many vlaues in hash table
        self.index = 0# initilising index
        self.list = [(0, l1), (1, l2), (2, l3), (3, l4), (4, l5), (5, l6), (6, l7), (7, l8), (8, l9)]# one big list to store all of the linked lists
    def algorithm(self, key):
        # creating the algorithm
        list1 = list(key)# takes in all of the charctaers of the key and turns it into a list
        Sum = 0
        for i in range(0, len(list1)):
            Sum += ord(list1[i])# finds unicode values for avery character in the key and adds them up
        self.index = Sum % self.length# creates the hash value
    def add(self, key, value):
        self.algorithm(key)
        # adding in vlaues to hash table
        for i in range(0, 9):
            row = self.list[i][0]# gets the indexes of all the rows
            if row == self.index:
                if row == 0:
                    l1.delete(key)# if there is an existing key with same name then it will overwrite it.
                    l1.add(key, value)
                    l1.view()
                    print("this was added in row 0")

                elif row == 1:
                    l2.delete(key)
                    l2.add(key, value)
                    l2.view()
                    print("this was added in row 1")

                elif row == 2:
                    l3.delete(key)
                    l3.add(key, value)
                    l3.view()
                    print("this was added in row 2")
                    self.number += 1
                    print(self.number)
                elif row == 3:
                    l4.delete(key)
                    l4.add(key, value)
                    l4.view()
                    print("this was added in row 3")
                elif row == 4:
                    l5.delete(key)
                    l5.add(key, value)
                    l5.view()
                    print("this was added in row 4")
                elif row == 5:
                    l6.delete(key)
                    l6.add(key, value)
                    l6.view()
                    print("this was added in row 5")
                elif row == 6:
                    l7.delete(key)
                    l7.add(key, value)
                    l7.view()
                    print("this was added in row 6")
                elif row == 7:
                    l8.delete(key)
                    l8.add(key, value)
                    l8.view()
                    print("this was added in row 7")
                else:
                    l9.delete(key)
                    l9.add(key, value)
                    l9.view()
                    print("this was added in row 8")

        else:
            pass
    def delete(self, key):
        self.algorithm(key)
        for i in range(0, self.length):
            row = self.list[i][0]# gets the indexes of all the rows
            if row == self.index:
                if row == 0:
                    l1.delete(key)
                    l1.view()
                elif row == 1:
                    l2.delete(key)
                    l2.view()
                elif row == 2:
                    l3.delete(key)
                    l3.view()
                elif row == 3:
                    l4.delete(key)
                    l4.view()
                elif row == 4:
                    l5.delete(key)
                    l5.view()
                elif row == 5:
                    l6.delete(key)
                    l6.view()
                elif row == 6:
                    l7.delete(key)
                    l7.view()
                elif row == 7:
                    l8.delete(key)
                    l8.view()
                else:
                    l9.delete(key)
                    l9.view()
    def find(self, key):
        self.algorithm(key)
        for i in range(0, self.length):
            row = self.list[i][0]# gets the indexes of all the rows
            if row == self.index:
                if row == 0:
                    l1.find(key)
                elif row == 1:
                    l2.find(key)
                elif row == 2:
                    l3.find(key)
                elif row == 3:
                    l4.find(key)
                elif row == 4:
                    l5.find(key)
                elif row == 5:
                    l6.find(key)
                elif row == 6:
                    l7.find(key)
                elif row == 7:
                    l8.find(key)
                else:
                    l9.find(key)
    def view(self):
        # prints all of the lists in order.
        l1.view()
        l2.view()
        l3.view()
        l4.view()
        l5.view()
        l6.view()
        l7.view()
        l8.view()
        l9.view()

            
        
                
        
    
    
# initilising all of the lists and then the hash table           
l1 = linked_list()
l2 = linked_list()
l3 = linked_list()
l4 = linked_list()
l5 = linked_list()
l6 = linked_list()
l7 = linked_list()
l8 = linked_list()
l9 = linked_list()
Hash = hash_table()
run = True# this is just used to add, delete, view, find and see how many items are in the hash table by just taking in inputs
while run:
    Input = str(input("what do you want to do with the Hashmap?"))
    if Input == "add()":
        key = str(input("enter key"))
        value = input("enter vlaleu")
        Hash.add(key, value)
    elif Input == "delete()":
        key = input("enter key to be deleted")
        Hash.delete(key)
    elif Input == "no.items()":
        print(Hash.number)
    elif Input == "view()":
        Hash.view()
    elif Input == "find()":
        key = input("please enter in your key to find")
        Hash.find(key)
    else:
        pass# if the input wasn't a command then just ignore it
        










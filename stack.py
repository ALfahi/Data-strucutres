class stack():
    def __init__(self):
        self.list = [1, 2, 3]# initialising list with some arbitary numbers
        self.head = self.list[-1]# initialises to the last value in list
        self.maxlen = 10
    def pop(self):
        if len(self.list) != 0:# can't pop stack if it is empty
            self.list.pop()
            if len(self.list) > 1:
                self.head = self.list[-1] # initialises to the last value in list
            else:
                self.head = "Null" # the head is empty
        else:
            print("underflow error")
    def push(self, value):
        if len(self.list) < self.maxlen:# can't add more vlaues into stack if it's full
            self.list.append(value)
            self.head = self.list[-1] # initialises to the last value in list
        else:
            print("overflow error!!!")
    def peek(self):
        print(self.head)# prints the vlaue at the top of the stack
    def isEmpty(self):
        if len(self.list) == 0:
            print("True")
        else:
            print("False")
    def isFull(self):
        if len(self.list) == self.maxlen:
            print("True")
        else:
            print("False")
        
    
Stack = stack()    
run = True
while run:# allows user to test out the stack at real time
    Input = str(input("what do you want to do with the stack?"))
    if Input == "pop()":
        Stack.pop()
    elif Input == "push()":
        value = int(input("please enter vlaue to be pushed into stack"))
        Stack.push(value)
    elif Input == "peek()":
        Stack.peek()
    elif Input == "isEmpty()":
        Stack.isEmpty()
    elif Input == "isFull()":
        Stack.isFull()
    elif Input == "view":# not a stakc function but in case if user wants to see whats in stack
        print(Stack.list)
    else:
        pass
    
        

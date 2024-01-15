class queue():
    def __init__(self):
        self.list = [1, 2, 3]# intitialising the list with some arbitary values; queue starts at three and ends at 1.
        self.top = self.list[-1]# initialises to the last value in list(first element to be removed)
        self.bottom = self.list[0]# first value
        self.maxlen = 10
    def dequeue(self):# remeoving items from queue
        if len(self.list) != 0:# can't delete if there is no items in queue
            self.list.pop()
            if self.top != self.bottom:
                self.top = self.list[-1] # initialises to the last value in list
            else:
                self.top = "Null" # the head is empty
        else:
            print("underflow error")
    def enqueue(self, value):
        if len(self.list) < self.maxlen:# makes sure you can't add in more vlaues than the max limit
            self.list.insert(0, value)
            self.bottom = self.list[0] # initialises to the last value in list
        else:
            print("overflow error!!!")
    def peek(self):
        print(self.top)# just prints value first in list(value that is about to be deleted when dequeued)
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
        
    
Queue = queue()    
run = True
while run:
    Input = str(input("what do you want to do with the queue?"))
    if Input == "dequeue()":
        Queue.dequeue()
    elif Input == "enqueue()":
        value = int(input("please enter vlaue to be pushed into queue"))
        Queue.enqueue(value)
    elif Input == "peek()":
        Queue.peek()
    elif Input == "isEmpty()":
        Queue.isEmpty()
    elif Input == "isFull()":
        Queue.isFull()
    elif Input == "view":# not a queue function but in case if user wants to see whats in stack
        print(Queue.list)
    else:
        pass

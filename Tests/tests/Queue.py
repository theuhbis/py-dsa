class Queue:
    size = int(input("input the length of your queue: "))
    queue = []
    start = True


    def enqueue(self):
        if len(self.queue) >= self.size:
            print("overflow, queue is full")
        else:
            input1 = int(input("Input the number: "))
            self.queue.append(input1)
            print("element has been inserted")

    def dequeue(self):
        if len(self.queue) == 0:
            print("underflow, queue is empty")
        else:
            self.queue.remove(self.queue[0])
            print("element has been removed")
            print(self.queue)

    def is_Empty(self):
        if len(self.queue) == 0:
            print("queue is empty")
        else:
            print(f"Queue is not empty {self.queue}")

    def peek(self):
        if len(self.queue) == 0:
            print("queue is empty and has no peek")
        else:
            print(self.queue[0])

    def start(self):
        while self.start:
            input2 = int(input("""What will you like to do to your queue:
                            1.Enqueue
                            2.Dequeue
                            3. find peek
                            4. check if queue is empty: """))
            if input2 == 1:
                self.enqueue()
                self.continuation()
            elif input2 == 2:
                self.dequeue()
                self.continuation()
            elif input2 == 3:
                self.peek()
                self.continuation()
            elif input2 == 4:
                self.is_Empty()
                self.continuation()
            else:
                print("enter a correct number")
                self.continuation()

    def continuation(self):
        input3 = input("Do you wish to continue Y for yes and N for no: ").upper()
        if input3 == "N":
            self.start = False
        elif input3 == "Y":
            self.start = True
        else:
            print("input the correct letter: ")
            self.continuation()

    def __init__(self):
        pass


obj = Queue()
obj.start()

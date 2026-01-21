class circularQueue:
   def __init__(self, maxsize):
        self.front = 0
        self.rear = -1
        self.queue = []
        self.size = 0 # elements in the queue
        self.maxsize = maxsize #size of the array(queue)
        # this next bit is important to make it work...but it feels a bit rubbish,
        #can this all be done without blank things in the list at the start?
        for i in range(maxsize):
          self.queue.append("")

   def isEmpty(self):
       if self.size == 0:
            return True
       else:
           return False

   def isFull(self):
       if self.size == self.maxsize:
          return True
       else:
          return False

   def enQueue(self, newItem):
       if self.size == self.maxsize:
           print('Queue Full')
       else:
           self.rear = (self.rear + 1) % self.maxsize # mod = remainder
           self.queue[self.rear]= newItem
           self.size = self.size + 1

   def deQueue(self):
       if self.size == 0:
           print('Queue Empty')
           item = null
       else:
           item = self.queue[self.front]
           self.queue[self.front] = ""
           self.front = (self.front + 1) % self.maxsize # mod = remainder
           self.size = self.size - 1

       return item
       
myQ = circularQueue(10)
for i in range(65,65+26):
  myQ.enQueue(chr(i))
print(myQ.queue)
myQ.deQueue()
myQ.deQueue()
myQ.deQueue()
myQ.deQueue()
print(myQ.queue)
myQ.enQueue("new thing")
print(myQ.queue)
myQ.enQueue("new thing2")
print(myQ.queue)

for i in range(7):
  thing = myQ.deQueue()
  print(thing)
 
print(myQ.queue)
for i in range(65,65+26):
  myQ.enQueue(chr(i))
print(myQ.queue)

for i in range(7):
  thing = myQ.deQueue()
  print(thing)

import DSAQueue

q1 = DSAQueue.CircularQueue()

q1.enqueue('Kai')
q1.enqueue('1')
q1.enqueue('2')
q1.enqueue('3')
q1.enqueue('4')

q1.display()

q1.dequeue()
q1.dequeue()
q1.dequeue()

q1.display()

q1.enqueue('DSA')
q1.enqueue(1002)
q1.dequeue()

q1.display()

q1.dequeue()
q1.enqueue('Tutorial')

q1.display()

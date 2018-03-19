class Queue:
	def __init__(self):
		self.queue=[]
	def isEmpty(self):
		return self.queue ==[]
	def enqueue(self,data):
		self.queue.append(data)
	def dequeue(self):
		data= self.queue[0]
		del self.queue[0]
		return data
	def peek(self):
		return self.queue[0]
	def sizeQueue(self):
		return len(self.queue)

		
		
		
queue=Queue()
queue.enqueue(6)
queue.enqueue(30)
queue.dequeue()
print(queue.queue)
queue.peek()
print(queue.queue)


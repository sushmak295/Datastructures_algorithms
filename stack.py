class Stack:
	def __init__(self):
		self.stack=[]
	def isEmpty(self):
		return self.stack == []
	def push(self,item):
		self.stack.append(item)
	def pop(self):
		data= self.stack[-1]
		del self.stack[-1]
		return data
	def peek(self):
		return self.stack[-1]
	def sizeStack(self):
		return len(self.stack)

		
stack=Stack()
stack.push(1)
stack.push(10)
print(stack.stack)
print(stack.peek())
print(stack.stack)
print(stack.pop())
print(stack.stack)

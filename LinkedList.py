class Node(object):
	def  __init__(self,data):
		self.data=data
		self.nextNode=None;
		
class LinkedList(object):
	def __init__(self):
		self.head=None
		self.size=0
	def remove(self,data):
		if self.head is None:
			return;
		else:
			self.size=self.size-1;
			currentNode =self.head;
			previousNode =None;
			while currentNode.data != data:
				PreviousNode =currentNode;
				currentNode =currentNode.nextNode;
			if  previousNode is None:
				self.head =currentNode.nextNode;
			else:
				previousNode.nextNode =currentNode.nextNode;
				
			
	def insertStart(self,data):
		self.size=self.size+1;
		newNode=Node(data)
		if not self.head:
			self.head=newNode;
		else:
			newNode.nextNode= self.head
			self.head=newNode
	
	def size(self):
		return self.size
	
	def size2(self):
		actualNode = self.head;
		size=0;
		while actualNode is not None:
			size+=1;
			actualNode =actualNode.nextNode;
		return size;
		
	def insertEnd(self,data):
		self.size= self.size +1;
		newNode =Node(data);
		actualNode=self.head;		
		while actualNode.nextNode is not None:
			actualNode =actualNode.nextNode;
			
		actualNode.nextNode =newNode;
	
	
	def traverseList(self):
		actualNode = self.head;
		while actualNode is not None:
			print(actualNode.data);
			actualNode = actualNode.nextNode;
			
llist=LinkedList()
llist.insertStart(12);
llist.insertStart(122);
llist.insertStart(3);
llist.insertEnd(31);
llist.traverseList();
	

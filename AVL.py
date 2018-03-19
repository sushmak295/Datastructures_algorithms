class Node(object):

	def __init__(self,data):
		self.data= data;
		self.hieght=0;
		self.leftChild=None;
		self.rightChild=None;

class AVL(object):
	
        def __init__(self):
                self.root =None;


        def insert(self,data):
                self.root=self.insertNode(data,self.root);


        def insertNode(self,data,node):
                if not node:
                        return Node(data);
                if data <node.data:
                        node.leftChild =self.insertNode(data,node.leftChild);
                else:
                        node.rightChild=self.insertNode(data,node.rightChild);
                        
                node.hieght=max(self.calcHieght(node.leftChild),self.calcHieght(node.rightChild))+1;
                
                return self.settleViolation(data,node);
        def removeNode(self,data,node):
                if not node:
                        return node;
                if data<node.data:
                        node.leftChild=self.removeNode(data,node.leftChild);
                elif data>node.data :
                        node.rightChild=self.removeNode(data,node.rightChild);
                else:
                        if not node.leftChild and not node.rightChild:
                                print('removing leaf node...');
                                del node;
                                return None;
                        if not node.leftChild:
                                print("Removing a node with single right child ");
                                tempNode = node.rightChild;
                                del node;
                                return tempNode;
                        elif not node.rightChild:
                                print("removing a node with single left child  ")
                                tempNode = node.leftChild;
                                del node;
                                return tempNode;
                        print("removing node with two children....")
                        tempNode=self.getPredeccor(node.leftChild);
                        node.data=tempNode.data;
                        node.leftChild=self.removeNode(tempNode.data,node.leftChild);

                
                if not node:
                        return node;
                
                node.hieght=max(self.calcHieght(node.leftChild),self.calcHieght(node.rightChild))+1;
                
                balance=self.calcBalance(node);
                
                if balance > 1 and data < node.leftChild.data:
                        print("left left heavy situation....");
                        return self.rotateRight(node);
                if balance < -1 and data >node.rightChild.data:
                        print('right right heavy situation....')
                        return self.rotateLeft(node);
                
                if balance > 1 and data >node.leftChild.data:
                        print("left right heavy situation.... ")
                        node.leftChild=self.rotateLeft(node.leftChild);
                        return self.rotateRight(node);
                if balance <-1 and data < node.rightChild.data:
                        print(" right  left  heavy situation.... ")
                        node.rightChild=self.rotateRight(node.rightChild);
                        return self.rotateLeft(node);
                return node;

        def settleViolation(self,data,node):
                balance=self.calcBalance(node);
                #case 1 --> left left heavy situation
                if balance > 1 and data < node.leftChild.data:
                        print("left left heavy situation....");
                        return self.rotateRight(node);
                if balance < -1 and data >node.rightChild.data:
                        print('right right heavy situation....')
                        return self.rotateLeft(node);
                
                if balance > 1 and data >node.leftChild.data:
                        print("left right heavy situation.... ")
                        node.leftChild=self.rotateLeft(node.leftChild);
                        return self.rotateRight(node);
                if balance <-1 and data < node.rightChild.data:
                        print(" right  leftheavy situation.... ")
                        node.rightChild=self.rotateRight(node.rightChild);
                        return self.rotateLeft(node);
                return node;

        def traverse(self):
                if self.root:
                        self.traverseInOrder(self.root);

        def traverseInOrder(self,node):
                if node.leftChild:
                        self.traverseInOrder(node.leftChild);

                        print(node.data)

                if node.rightChild:
                        self.traverseInOrder(node.rightChild);

        def calcHieght(self,node):
                if not node:
                        return -1
                return node.hieght;


        def calcBalance(self,node):
                if not node:
                        return 0;
                return self.calcHieght(node.leftChild)-self.calcHieght(node.rightChild);


        def rotateRight(self,node):
                print('rotating to the right :',node.data)
                tempLeftChild=node.leftChild
                t = tempLeftChild.rightChild;
                
                tempLeftChild.rightChild=node;
                node.leftChild=t;
                
                node.hieght=max(self.calcHieght(node.leftChild),self.calcHieght(node.rightChild))+1;
                tempLeftChild.hieght=max(self.calcHieght(tempLeftChild.leftChild),self.calcHieght(tempLeftChild.rightChild))+1;
                return tempLeftChild;


        def rotateLeft(self,node):
                print('rotating to the right :',node.data)
                tempRightChild=node.rightChild
                t = tempRightChild.leftChild;
                
                tempRightChild.leftChild=node;
                node.rightChild=t;
                
                node.hieght=max(self.calcHieght(node.leftChild),self.calcHieght(node.rightChild))+1;
                tempRightChild.hieght=max(self.calcHieght(tempRightChild.leftChild),self.calcHieght(tempRightChild.rightChild))+1;
                return tempRightChild;
	
	


class Heap(object):
    heap_size=10;
    def __init__(self):
        self.heap=[0]*Heap.heap_size;
        self.currentposition=-1;
            
    def insert(self,item):
        if self.isfull():
                print "Heap is full"
                return
        self.currentposition=self.currentposition+1
        self.heap[self.currentposition]=item;
        #print "before fixup:",self.heap
        self.fixup(self.currentposition);
        #print "after fixup:",self.heap
    def fixup(self,index):#considering maxheap
        parent_index =int((index-1)/2);
        while parent_index>=0 and self.heap[parent_index] < self.heap[index]:
                #if the parent is of smaller value;swap parent and child and repeat until the heap is balanced.
                temp=self.heap[index]
                self.heap[index]=self.heap[parent_index]
                self.heap[parent_index]=temp;
                index=parent_index
                parent_index=int((parent_index-1)/2);#update parent_index #doubt
            
    def heapsort(self):
        for i in range(0,self.currentposition+1):
                temp=self.heap[0]
                print temp
                self.heap[0]=self.heap[self.currentposition-i]
                self.heap[self.currentposition-i]=temp
                self.fixdown(0,self.currentposition-i-1)
                    
                    
                    
    def fixdown(self,start_ind,last_ind):
        while start_ind<last_ind:
                left_child=2*start_ind+1
                right_child=2*start_ind+2
                if left_child <=last_ind:
                        child_to_swap=None
                        if right_child >last_ind:
                                child_to_swap=left_child
                        else:
                                if self.heap[left_child]>self.heap[right_child]:
                                        child_to_swap =left_child
                                else:
                                        child_to_swap=right_child
                        if self.heap[start_ind]<self.heap[child_to_swap]:
                                temp=self.heap[start_ind]
                                self.heap[start_ind]=self.heap[child_to_swap]
                                self.heap[child_to_swap]=temp
                        else:
                                break
                        start_ind=child_to_swap
                else:
                        break
                            
                            
                                    
                                    
                    


    def isfull(self):
        if self.currentposition==Heap.heap_size:
                return True
        else:
                return False
	


if __name__=="__main__":
    heap=Heap()
    heap.insert(23)
    heap.insert(5)
    heap.insert(100)
    heap.insert(2)
    heap.insert(210)
    heap.heapsort()

	

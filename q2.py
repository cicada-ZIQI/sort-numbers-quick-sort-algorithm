class Node:
    def __init__(self,element,pointer):
        self.element=element
        self.pointer=pointer

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def add(self,e):
        newest=Node(e,None)
        newest.pointer=self.head
        self.head=newest

    def create(self):
        self.add(6)
        self.add(7)
        self.add(3)
        self.add(10)
        self.add(12)
        self.add(2)
        self.add(9)

    #output the element of each node
    def output(self,node):
        pointer=self.head
        while pointer:
            print(pointer.element,end=" ")
            pointer=pointer.pointer

#use quick sort algorithsm to sort numbers
def quicksort(first_node,last_node=None):
    #if there are more than one element in a sub-linkedlist, then this sub-linkedlist need to be sorted
    if first_node != last_node:
        #for each compare, set the first element of the linkedlist as the pivot
        pivot=first_node.element
        # the element of node "compare" need to be compared with the pivot
        compare=first_node.pointer
        #if the value of the node "compare" is smaller than the pivot ,then the value of the compare need to be reset by the value of node "standard"
        standard=first_node
        # since compare need to be continuously moved to the next node, so the end of a turn of comparison is when the compare node == the last node
        while compare != last_node:
            #if the element of node "compare" is larger than pivot, then no need to do anything, just directly move to the next node
            if compare.element >= pivot:
                compare=compare.pointer
                continue
            # if the element of node"compare" is smaller than pivot, the value of the node finally need to be set on the left of pivot
            elif  compare.element < pivot:
                standard=standard.pointer
                # change the value of the next node of node"standard" and the node "compare", thus the smaller values is on the left while the larger
                # value is on the right. Now, for all the values that have been compared: values that are larger than the pivot are on the right of node"standard
                # while values that are smaller than the pivot are on the left of the node "standard", and the value of node "standard" is smaller than pivot
                standard.element,compare.element=compare.element,standard.element
                compare=compare.pointer
        # finally change the value of node "standard" and pivot, then all the values on the left of pivot is less than pivot, values
        #on the right are larger than pivot
        first_node.element,standard.element=standard.element,first_node.element
        # pivot is in the right place, then continuouly to sort the rest sub-linkedlist which are on the left and right of the pivot respectively
        quicksort(first_node,standard)
        quicksort(standard.pointer,last_node)

L=LinkedList()
L.create()
#use the reference of the first node as the input of function
quicksort(L.head)
print("Before sorting, the numbers are: 6 5 3 10 12 2 4")
print("After sorting, the numbers are: ",end="")
L.output(L.head)
print("")
#ouput the reference of the first node of the linkedlist thant is sorted
print("The reference of the first node is:", L.head)
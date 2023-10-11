class Node():
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

class linkedlist():
    def __init__(self,num_node):              
        count=0
        for i in range(1,num_node):
            if count == 0:
                p=self.head=Node(i)
                count +=1
            else:
                p.next=Node(i)
                p=p.next
    def __str__(self):
        p=self.head
        out=''
        while p:
            out+= str(p.val)+str(p.next)+ "\n"
            p=p.next
        return out
    
    def traverse(self,n):
        p=self.head
        count=1
        while count <n:
            p=p.next
            count+=1
        return p
    
    def delete_node(self,root):
        if not root:
            return
       # print(root,root.val,root.next,root.next.val)
        if  root.next:
            root.val=root.next.val
            root.next=root.next.next
            #print(root,root.val,root.next,root.next.val)
        else:
            del root
            root=None
       # print(root,root.val)
        #return self.head
            


ll=linkedlist(10)
root=ll.traverse(8)
print(ll)
print(root,root.val)
ll.delete_node(root)
print(ll)


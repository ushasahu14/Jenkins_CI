class Node():
    def __init__(self,value, left=None, right=None):
        self.val=value
        self.left=left
        self.right=right

class traversal():
    def inorder(root,l=[]):
        if not root:
            return l
        elif not root.left and not root.right:
            l.append(root.val)
        elif root.left:
            traversal.inorder(root.left,l)
        else:
            traversal.inorder(root.right,l)
        return l
    
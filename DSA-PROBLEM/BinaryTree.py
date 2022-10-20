#this program is having the all sorts of the possible question from a Binary tree

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Node_linked():
    def __init__(self,data):
        self.data=data
        self.next=None

class Binary():

    def __init__(self,data):
        self.root=Node(data)
        self.head=None

    def inorder(self,start,traversal):
        if(start is None):
            return

        self.inorder(start.left,traversal)
        traversal.append(start.data)
        self.inorder(start.right,traversal)

        return traversal

    def preorder(self, start, traversal):
        if (start is None):
            return
        traversal.append(start.data)
        self.preorder(start.left, traversal)
        self.preorder(start.right, traversal)

        return traversal

    def postorder(self, start, traversal):
        if (start is None):
            return

        self.postorder(start.left, traversal)
        self.postorder(start.right, traversal)
        traversal.append(start.data)

        return traversal

    def levelorder(self, start):
        queue=[start]
        traversal=[]
        while(len(queue)!=0):
            hold=queue.pop(0)
            traversal.append(hold.data)
            if(hold.left is not None):
                queue.append(hold.left)

            if (hold.right is not None):
                queue.append(hold.right)
        return(traversal)

    def height(self,start):
        if(start is None): return 0

        return 1+max(self.height(start.left),self.height(start.right))

    def left_view_m1(self,start,traversal,level):

        if(start is None): return

        if(len(traversal)<level+1): traversal.append(start.data)

        left=self.left_view_m1(start.left,traversal,level+1)
        right=self.left_view_m1(start.right,traversal,level+1)

        return traversal

    def left_view_m2(self,start):
        queue=[start]
        traversal=[]

        while(len(queue)!=0):
            length=len(queue)

            for i in range(length):
                hold=queue.pop(0)
                if(i==0):
                    traversal.append(hold.data)
                if(hold.left):
                    queue.append(hold.left)
                if(hold.right):
                    queue.append(hold.right)
        return(traversal)

    def right_view_m1(self,start,traversal,level):

        if(start is None): return

        if(len(traversal)<level+1): traversal.append(start.data)

        right = self.right_view_m1(start.right, traversal, level + 1)
        left=self.right_view_m1(start.left,traversal,level+1)


        return traversal

    def right_view_m2(self,start):
        queue=[start]
        traversal=[]

        while(len(queue)!=0):
            length=len(queue)

            for i in range(length):
                hold=queue.pop(0)
                if(i==length-1):
                    traversal.append(hold.data)
                if(hold.left):
                    queue.append(hold.left)
                if(hold.right):
                    queue.append(hold.right)
        return(traversal)

    def Lca(self,start,n1,n2):
        traverse_1=self.find(start,n1,[])
        traverse_2=self.find(start,n2,[])
        print(traverse_1,traverse_2)

    def find(self,start,n1,traverse):
        if(start is None): return
        if(start.data==n1):
            self.back(traversal)
            return
        traverse.append(start.data)
        left=self.find(start.left,n1,traverse)
        right = self.find(start.right, n1, traverse)
        traverse.pop()
        return

    def lca(self,start,n1,n2):
        if(start is None): return

        if(start.data==n1 or start.data==n2): return start.data

        left=self.lca(start.left,n1,n2)
        right = self.lca(start.right, n1, n2)

        if(left is None): return right
        if(right is None): return left

        return start.data

    def longest_path(self,start):

        if(start is None): return 0

        leftHeight=self.height(start.left)
        rightHeight=self.height(start.right)
        calculate=leftHeight+rightHeight+1

        left=self.longest_path(start.left)
        right = self.longest_path(start.right)

        return max(calculate,max(left,right))

    def top_view(self,start):

        count=0
        queue=[start]

        dict={}
        data=[0]

        while(len(queue)!=0):

            hold=queue.pop(0)
            count=data.pop(0)
            if(count not in dict):
                dict[count]=hold.data
            if(hold.left):
                queue.append(hold.left)
                data.append(count-1)
            if(hold.right):
                queue.append(hold.right)
                data.append(count+1)

        return dict.values()

    def bottom_view(self,start):

        queue=[start]
        data=[0]
        dict={}
        while(len(queue)!=0):
            hold=queue.pop(0)
            count=data.pop(0)

            dict[count]=hold.data

            if (hold.left):
                queue.append(hold.left)
                data.append(count - 1)
            if (hold.right):
                queue.append(hold.right)
                data.append(count + 1)
        return dict.values()


    def num_nodes(self,start):
        if(start is None): return 0
        return 1+self.num_nodes(start.left)+self.num_nodes(start.right)

    def max_value(self,start):
        if (start is None): return 0
        return max(start.data,max(self.num_nodes(start.left) , self.num_nodes(start.right)))



#creating the binary tree
tree=Binary(50)
tree.root.left=Node(20)
tree.root.right=Node(70)
tree.root.left.left=Node(11)
tree.root.left.right=Node(30)
tree.root.right.left=Node(60)
tree.root.left.right.right=Node(40)
tree.root.left.right.left=Node(25)

print(tree.inorder(tree.root,[]))#inorder

print(tree.preorder(tree.root,[]))#preorder

print(tree.postorder(tree.root,[]))#postorder

print(tree.levelorder(tree.root))#levelorder

print(tree.height(tree.root))#height of the tree

print(tree.left_view_m1(tree.root,[],0))#left view of the tree
print(tree.left_view_m2(tree.root))

print(tree.right_view_m1(tree.root,[],0))#right view of the tree
print(tree.right_view_m2(tree.root))

print(tree.lca(tree.root,11,30))#lowest common ancestor of the two values
print(tree.lca(tree.root,11,25))
print(tree.lca(tree.root,30,60))

print(tree.longest_path(tree.root))#longest path from left to right in the binary tree

print(tree.top_view(tree.root))#top view of the binary tree

print(tree.bottom_view(tree.root))#bottom view of the binary

print(tree.num_nodes(tree.root))#number of nodes in the binary tree

print(tree.max_value(tree.root))#max value in the binary tree

#print(tree.linked_list(tree.root))

#tree from inorder preorder,tree to linked list,

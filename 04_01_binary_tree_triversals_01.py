# implement in-order, pre-order and post-order traversals of a binary tree
import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class Tree:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
    
    def InOrderT(self,i,ans):
        if self.n == 0:
            return
        if i == -1:
            return
        Root = i
        self.InOrderT(self.left[Root],ans)
        ans.append(str(self.key[Root]))
        self.InOrderT(self.right[Root],ans)

    def PreOrderT(self,i,ans):
        if self.n == 0:
            return
        if i == -1:
            return
        Root = i
        ans.append(str(self.key[Root]))
        self.PreOrderT(self.left[Root],ans)
        self.PreOrderT(self.right[Root],ans)    

    def PostOrderT(self,i,ans):
        if self.n == 0:
            return
        if i == -1:
            return
        Root = i
        self.PostOrderT(self.left[Root],ans)
        self.PostOrderT(self.right[Root],ans)  
        ans.append(str(self.key[Root]))

def main():
    tree = Tree()
    tree.read()
    ans1, ans2, ans3 = [], [], []
    tree.InOrderT(0,ans1)
    tree.PreOrderT(0,ans2)
    tree.PostOrderT(0,ans3)
    for i in [ans1,ans2,ans3]:
        if len(i) == 0:
            print(' ')
        else:
            print(' '.join(i))

threading.Thread(target=main).start()



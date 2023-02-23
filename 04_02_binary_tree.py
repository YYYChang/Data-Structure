# check if input is a binary tree
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

    def Binary_ck(self,i):
        if self.n == 0:
            return (True,0,0)
        
        key = self.key[i] 
        l_id, r_id = self.left[i], self.right[i]
        l_isbinary, r_isbinary = True, True
        if l_id != -1:
            l_max, l_min = self.key[l_id], self.key[l_id]
            if key < l_max:
#                print(i,l_id,r_id,'A')
                return (False,0,0)
            else: 
#                print(i,l_id,r_id,'B')
                l_isbinary, l_max, l_min = self.Binary_ck(l_id)
        else:
#            print(i,l_id,r_id,'C')
            l_max, l_min = key, key
        
        if r_id != -1:
            r_max, r_min = self.key[r_id], self.key[r_id]
            if key > r_max:
#                print(i,l_id,r_id,'D')
                return (False,0,0)
            else:
#                print(i,l_id,r_id,'E')
                r_isbinary, r_max, r_min = self.Binary_ck(r_id)
        else: 
#            print(i,l_id,r_id,'F')
            r_max, r_min = key, key
        
        if l_isbinary and r_isbinary is True:
            if r_min < key or l_max > key:
#                print(i,l_id,r_id,'G',key,r_min,l_max)
                return (False,0,0)
            else:
#                print(i,l_id,r_id,'H',r_max,l_min)
                return (True,r_max,l_min)
        else:
#            print(i,l_id,r_id,'I')
            return (False,0,0)

def main():
    tree = Tree()
    tree.read()
    if tree.Binary_ck(0)[0] is True:
        print('CORRECT')
    else:
        print('INCORRECT')

threading.Thread(target=main).start()

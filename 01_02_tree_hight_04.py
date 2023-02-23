# store the tree and compute its height
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def tree_hight(n,mls):
    root_id = tree_create(n,mls)
    return max_tree_level(n,mls,root_id)

def tree_create(n,mls):
    for i in range(n):
        mls[i] = [mls[i]]
    for i in range(n):
        j = mls[i][0]   
        if j != -1:
            mls[j].append(i)
        else:
            root = i
    return root

def max_tree_level(n,mls,root_id):
    par_chd = mls[root_id]
    size = len(par_chd)

    if size == 1:
        return 1
    else:
        tree_lvl = 0
        for i in par_chd[1:]:
            lvl = max_tree_level(n,mls,i)
            if lvl > tree_lvl:
                tree_lvl = lvl

    return tree_lvl + 1
    
def main():
    n = int(input())
    mls = list(map(int,input().split()))
    print(tree_hight(n,mls))
threading.Thread(target=main).start()
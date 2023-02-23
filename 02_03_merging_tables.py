# simulate a sequence of merge operations with tables in a database
# n = tables, m = merge queries  merge_ls = (destination_i,source_i)
import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

def Find_root(i,parent_ls):
    parent = parent_ls[i]
    if  i != parent:
        parent_ls[i] = Find_root(parent,parent_ls)
    return parent_ls[i]

def merging_tables(n,m,rows_ls,merge_ls):
    parent_ls = []
    max_row = max(rows_ls)
    for i in range(n):
        parent_ls.append(i)
    for k,v in  merge_ls: # index + 1
        dest = k - 1
        source = v - 1
#        print('1:',dest,source)
        if dest != parent_ls[dest]:
            dest = Find_root(dest,parent_ls)
        if source != parent_ls[source]:
            source = Find_root(source,parent_ls)

        if dest != source:
            rows_ls[dest] += rows_ls[source]
            rows_ls[source] = 0 
        
        if rows_ls[dest] > max_row:
            max_row = rows_ls[dest]
        parent_ls[source] = dest
#        print('2:',rows_ls,parent_ls)
        print(max_row)

def main():
    n, m = map(int,input().split())
    rows_ls = list(map(int,input().split()))
    merge_ls = []
    for i in range(m):
        k, v = map(int,input().split())
        merge_ls.append((k,v))
    merging_tables(n,m,rows_ls,merge_ls)
threading.Thread(target=main).start()
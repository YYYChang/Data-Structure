# simulate a program that processes a list of jobs in parallel.
# n = thread qty. m = job qty. pt_lst = proccess t of i-th job
# heap parent(i) = (i-1)/2 lchild(i) = 2i+1 rchid = 2i+2
def sift_down(n,pos_id,H): # n = qty in H, pos_id = index
    lch_id = 2 * pos_id + 1 # index
    rch_id = 2 * pos_id + 2 # index
    max_id = pos_id
    if lch_id <= n - 1 and H[lch_id] < H[max_id]:
        max_id = lch_id

    if rch_id <= n - 1 and H[rch_id] < H[max_id]:
        max_id = rch_id

    if max_id != pos_id:
        temp = H[pos_id]
        H[pos_id] = H[max_id]
        H[max_id] = temp
        sift_down(n,max_id,H)

def sift_up(pos_id,H):
    par_id = (pos_id - 1) // 2
    while pos_id > 0 and H[par_id] > H[pos_id]:
        temp = H[pos_id]
        H[pos_id] = H[par_id]
        H[par_id] = temp
        pos_id = par_id
        par_id = (pos_id - 1) // 2

def built_heap(n,H):
    for i in range(n // 2):
        pos_id = n // 2 - 1 - i # index
        sift_down(n,pos_id,H)

def insert(num,H):
    H.append(num)
    pos_id = len(H) - 1
    sift_up(pos_id,H)

def extract_min(H):
    val = H[0]
    H[0] = H[-1]
    H.pop()
    n = len(H)
    sift_down(n,0,H)
    
    return val


def parallel_processing(n,m,pt_lst):
    from collections import deque
    free_thr = deque() # free thread
    wk_thr = deque() # working thread (avt,idex)
    for i in range(n):
        free_thr.append(i)
    built_heap(n,free_thr)
    
    thrav_t = 0 # time for next thread available
    for i in range(m): # iterate through all jobs
        rq_t = pt_lst[i] # current job required processing time
#        print('1:',i,rq_t,free_thr,wk_thr)
        if len(free_thr) == 0:
            thrav_t = wk_thr[0][0]
            while wk_thr and wk_thr[0][0] == thrav_t:
                id = extract_min(wk_thr)         
                insert(id[1],free_thr)
    
        thr_id = free_thr[0]
        pt_lst[i] = (thr_id,thrav_t)
        fin_t = thrav_t + rq_t
        if fin_t > thrav_t:
            extract_min(free_thr)
            insert((fin_t,thr_id),wk_thr)
#        print('2:',i,pt_lst[i],free_thr,wk_thr)

if __name__ == '__main__':
    n, m = map(int,input().split())
    pt_lst = list(map(int,input().split()))
    parallel_processing(n,m,pt_lst)
    for k,v in pt_lst:
        print(k,v)

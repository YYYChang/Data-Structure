# create a heap from the array you want to sort
# parent(i) = (i-1)/2 lchild(i) = 2i+1 rchid = 2i+2

def sift_down(n,pos_id,H):
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
        H[n] += 1
        H.append((pos_id,max_id))
        # print(H)
        sift_down(n,max_id,H)


def built_heap(n,H):
    H.append(0)
    for i in range(n//2):
        pos_id = (n)//2 - 1 - i # index
        sift_down(n,pos_id,H)

if __name__ == '__main__':
    n = int(input())
    H = list(map(int,input().split()))
    built_heap(n,H)
    swap_ls = H[n:]
    swap_t = swap_ls[0]
    print(swap_t)
    if swap_t > 0:
        for k,v in swap_ls[1:]:
            print(k,v)

def slide_max(m,n,als):
    from collections import deque
    val = []
    big_ls = deque()
    l = 0
    for i in range(n):
        while len(big_ls) > 0 and als[big_ls[-1]] <= als[i]:
            big_ls.pop()
        big_ls.append(i)

        if l > big_ls[0]:
            big_ls.popleft()
        
        if i >= m-1:
            max_id = big_ls[0]
            val.append(als[max_id])
            l += 1
           
    return val

if __name__=='__main__':
    n = int(input())
    als = list(map(int,input().split()))
    m = int(input())
    ans = list(map(str,slide_max(m,n,als)))
    print(' '.join(ans))
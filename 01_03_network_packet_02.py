# implement a program to simulate the processing of network packets
def network_process(buf,p_qty,p_ls):
    curav_t, cur_b, cur_ped = 0, buf, []
    for i in range(p_qty):
        cur_t, pcs_t = p_ls[i][0], p_ls[i][1]
        if curav_t <= cur_t:
            curav_t = cur_t + pcs_t
            cur_ped.append(curav_t)
            p_ls[i] = str(cur_t)
        else:
#            temp = []
#            for j in cur_ped:
#                fi_t = j 
#                if fi_t > cur_t:
#                    temp.append(fi_t)
#            cur_ped = temp
            cur_b = buf - len(cur_ped)
            if cur_b > 0:            
                p_ls[i] = str(curav_t)
                curav_t += pcs_t
                cur_ped.append(curav_t)
            elif cur_b == 0 and cur_ped[0] <= cur_t:
                cur_ped.pop(0)
                p_ls[i] = str(curav_t)
                curav_t += pcs_t
                cur_ped.append(curav_t)
            else:
                p_ls[i] = '-1'

if __name__ == '__main__':
    buf, p_qty = map(int,input().split())
    if p_qty == 0: quit()
    
    p_ls = []
    for i in range(p_qty) :
        arr_t, pr_t = map(int,input().split())
        p_ls.append((arr_t,pr_t))
    network_process(buf,p_qty,p_ls)
    ans = p_ls
    for i in ans:
        print(i)

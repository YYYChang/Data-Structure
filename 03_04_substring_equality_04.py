# check if two substrings of 𝑠 are equal
# use p1, p2 to avoid collision
def cpr_substring(T,n,cpr_ls): 
    T_num = len(T)

    # p1, p2 x use for PolyHash
    p1, p2, x = 1000000007, 1000000009, 2633

    # create list for substring[:i+1] PolyHash  
    substr_h_ls = []
    for i in range(T_num):
        substr_h_ls.append(0)

    for i in range(T_num):
        if i == 0:
            h1_substr, h2_substr = hash_fn(p1,p2,T[i])
        else:
            T_h1, T_h2 = hash_fn(p1,p2,T[i])
            h1_substr = (x * substr_h_ls[i-1][0] + T_h1) % p1 
            h2_substr = (x * substr_h_ls[i-1][1] + T_h2) % p2
        substr_h_ls[i] = (h1_substr,h2_substr)
#    print('1:',substr_h_ls)

    # pre caculate x^p
    x_p_dic = [(1,1)]
    for i in range(T_num):
        x_p_dic.append((1,1))
    x_p1, x_p2 = 1, 1 
    for i in range(1,T_num+1):
        x_p1 = x_p1 * x % p1
        x_p2 = x_p2 * x % p2
        x_p_dic[i] = (x_p1,x_p2) # x_p_dic[i] = (x ** i % p1, x ** i % p2 )
#    print('2:',x_p_dic)

    # compare substring
    ans = []
    for i in range(n):
        i1, i2, P_num = cpr_ls[i] # string start index1, index2
        if i2 == i1:
            ans.append('Yes')
            continue
        if i1 == 0:
            h1_bef_i1, h2_bef_i1 = 0, 0
        else:
            h1_bef_i1, h2_bef_i1 = substr_h_ls[i1-1]
        if i2 == 0:
            h1_bef_i2, h2_bef_i2 = 0, 0
        else:
            h1_bef_i2, h2_bef_i2 = substr_h_ls[i2-1]
        h1_i1end, h2_i1end = substr_h_ls[i1 + P_num -1]
        h1_i2end, h2_i2end = substr_h_ls[i2 + P_num -1]
        str1_h1 = (h1_i1end - h1_bef_i1 * x_p_dic[P_num][0] % p1) % p1
        str1_h2 = (h2_i1end - h2_bef_i1 * x_p_dic[P_num][1] % p2) % p2
        str2_h1 = (h1_i2end - h1_bef_i2 * x_p_dic[P_num][0] % p1) % p1
        str2_h2 = (h2_i2end - h2_bef_i2 * x_p_dic[P_num][1] % p2) % p2
        if str1_h1 == str2_h1 and str1_h2 == str2_h2:
            string_1 = T[i1:i1+P_num]
            string_2 = T[i2:i2+P_num]
            if string_1 == string_2:
                ans.append('Yes')
                continue
        ans.append('No')
    
    return ans

def hash_fn(p1,p2,string):
    h1, h2 = 0, 0
    x = 2633
    length = len(string)
    for i in range(length):
        S = ord(string[i])
        h1 = (h1 * x + S) % p1
        h2 = (h2 * x + S) % p2
    return (h1 % p1,h2 % p2)

if __name__ == '__main__':
    T = input()
    n = int(input())
    if n == 0:
        quit()
    cpr_ls = []
    for i in range(n):
        a, b, c = map(int,input().split())
        cpr_ls.append((a,b,c)) # index1, index2, length
    ans = cpr_substring(T,n,cpr_ls) 
    for i in ans:
        print(i)

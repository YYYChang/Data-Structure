# implement the Rabin–Karp’s algorithm for searching the given pattern in the given text
def find_substring(P,T): 
    P_num, T_num = len(P), len(T)

    # p, x use for PolyHash
    p, x = 1000000007, 263

    # create list for T[i] character PolyHash
    T_h = []
    for i in T:
        T_h.append(hash_fn(p,i))

    # pre caculate x^p
    x_p = 1
    for i in range(P_num):
        x_p = x_p * x % p

    # create list for substring PolyHash   
    substr_h_ls = []
    for i in range(T_num-P_num+1):
        substr_h_ls.append(0)

    for i in range(T_num-P_num+1):
        j = T_num - P_num - i
        substr = T[j:j+P_num]
        if i == 0:
            h_substr = hash_fn(p,substr)
        else:
            h_substr = (x * substr_h_ls[j+1] + T_h[j] - x_p * T_h[j+P_num]) % p
        substr_h_ls[j] = h_substr
    
    # compare patter with substring
    h_P = hash_fn(p,P)
    match_ls = []
    for i in range(T_num-P_num+1):
        substr_h = substr_h_ls[i]
        if substr_h == h_P:
            if T[i:i+P_num] == P:
                match_ls.append(str(i))
    
    return match_ls

def hash_fn(p,string):
    h = 0 
    x = 263
    length = len(string)
    for i in range(length):
        j = length - 1 - i
        S = ord(string[j])
        h = (h * x + S) % p
    return h % p

if __name__ == '__main__':
    P = input()
    T = input()
    ans = find_substring(P,T) # P pattern, T text
    if len(ans) == 0:
        print(' ')
    else:
        print(' '.join(ans))

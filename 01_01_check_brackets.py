# implement a feature for a text editor to find errors in the usage of brackets in the code.
def chk_brk(ipstr) :
    blst = []
    strl = len(ipstr)
    stl = ['(','[','{']
    edl = [')',']','}']

    for i in range(strl) :
        char = ipstr[i]
        if char in stl :
            blst.append((char,i))
        elif char in edl :
            if len(blst) == 0 : return i+1
            end = blst.pop()
            if (char == ')' and end[0] != '(') : return i+1
            elif (char == ']' and end[0] != '[') : return i+1 
            elif (char == '}' and end[0] != '{') : return i+1

    if len(blst) != 0 : return blst[0][1]+1
    return 'Success'

if __name__ == '__main__':
    ipstr = input()
    print(chk_brk(ipstr))
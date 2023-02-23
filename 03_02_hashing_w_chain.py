# hashing chain h(S) use: given m, p = 1 000 000 007, x = 263
class hashing_chain:
    def __init__(self,size):
        from collections import deque
        self.l = []
        for i in range(size):
            self.l.append(deque())
    def Add(self,number,string):
        exist = self.l[number]
        if string not in exist:
            exist.appendleft(string)
            self.l[number] = exist
    def Find(self,number,string):
        exist = self.l[number]
        if string in exist:
            return 'yes'
        else: 
            return 'no'
    def Del(self,number,string):
        exist = self.l[number]
        if string in exist:
            exist.remove(string)
            self.l[number] = exist
    def Check(self,number):
        exist = self.l[number]
        return ' '.join(exist)

def hash_fn(m,string):
    h = 0 
    p, x = 1000000007, 263
    length = len(string)
    for i in range(length):
        S = ord(string[i])
        h += S * x ** i 
    return h % p % m

if __name__ == '__main__':
    m = int(input())
    n = int(input())
    hashchain, ans = hashing_chain(m), []
    for i in range(n):
        cmd = input().split()
        if cmd[0] == 'add':
            number = hash_fn(m,cmd[1])
            hashchain.Add(number,cmd[1])
        elif cmd[0] == 'find':
            number = hash_fn(m,cmd[1])
            ans.append(hashchain.Find(number,cmd[1]))
        elif cmd[0] == 'del':
            number = hash_fn(m,cmd[1])
            hashchain.Del(number,cmd[1])
        elif cmd[0] == 'check':
            ans.append(hashchain.Check(int(cmd[1])))
    for i in ans:
        print(i)
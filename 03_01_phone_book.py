# phone book manager with fn Add(number name) Find(number) Del(number)
class phone_book:
    def __init__(self):
        self.d = dict()
    def Add(self,number,name):
        self.d[number] = name
    def Find(self,number):
        if number in self.d:
            return self.d[number]
        else: 
            return 'not found'
    def Del(self,number):
        if number in self.d:
            del self.d[number]

if __name__ == '__main__':
    n = int(input())
    Telbook = phone_book()
    ans = []
    for i in range(n):
        cmd = input().split()
        if cmd[0] == 'add':
            Telbook.Add(cmd[1],cmd[2])
        elif cmd[0] == 'find':
            ans.append(Telbook.Find(cmd[1]))
        elif cmd[0] == 'del':
            Telbook.Del(cmd[1])
    for i in ans:
        print(i)





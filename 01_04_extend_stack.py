# implement a stack that supports finding the maximum value, push, pop
# and to ensure that all operations still work in constant time.
def stack_interf(cmd_qty,cmd_ls):
    stack = []
    for i in cmd_ls:
        if i[0] == 'push':
            num = int(i[1])
            if len(stack) == 0:
                stack.append((num,num))
            else:
                max = stack[-1][1]
                if num > max:
                    max = num
                stack.append((num,max))
        elif i[0] == 'pop':
            if len(stack) > 0:
                stack.pop()
        elif i[0] == 'max':
            print(stack[-1][1])

if __name__ == '__main__':
    cmd_qty = int(input())
    cmd_ls = []
    for i in range(cmd_qty):
        command = input().split()
        cmd_ls.append(command)

    stack_interf(cmd_qty,cmd_ls)
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())
arr=[] #initialize list
for i in range(n):
    args = raw_input().split(" ")
    #test cases
    if args[0]=='insert':
        arr.insert(int(args[1]),int(args[2]))
    elif args[0]=='print':
        print arr
    elif args[0]=='remove':
        arr.remove(int(args[1]))
    elif args[0]=='append':
        arr.append(int(args[1]))
    elif args[0]=='sort':
        arr.sort()
    elif args[0]=='pop':
        arr.pop()
    elif args[0]=='reverse':
        arr.reverse()
    else:
        print 'invalid input'

print arr

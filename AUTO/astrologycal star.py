inp = int(input("please enter your number : "))
bolin_inp = int(input('please enter 1 for true and 0 for false : '))
if bolin_inp == 1:
    for i in range(1,inp+1):
        print('*' * i)
elif bolin_inp== 0:
    for i in range(inp,0,-1):
        for j in range(1,1+i):
            print ("*",end="")
        print()





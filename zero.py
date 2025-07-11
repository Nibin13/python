#input[0,1,0,2,3]
#output[1,2,3,0,0]

inp = input("enter the list: ")
num = inp.split(',')
print(num)
output=[]
outputt=[]
for i in num:
    if i =='0':
        output.append(i)
    else:
        outputt.append(i)
out=outputt+output
print(out)            

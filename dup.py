# read an array
#seperate numbers
#if same number found iterate
from typing import List
class numbers():
    def read_numbers(self,num:list[int])->bool:
     
     for i in range(0,len(num)):
           for j in range(i+1,len(num)):
               if num[i]==num[j]:
                   return False
               else:
                   continue
     return True  
dup=numbers()
numm=list(map(int,input("Enter the numbers: ").split(',')))
print(dup.read_numbers(numm))

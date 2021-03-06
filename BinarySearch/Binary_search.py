"""
Algorithm:
1- import libraries
2- create a list of random numbers from 0 to 100 with intervals of 2 in 2
3- number entry by the user
4-the program checks if the number entered is contained in the list and owes it to two equal parts
5 - find the number in the subarrays
"""



import random
from random import choices,sample

lista = []
size = 50
x = range(0,100,2)
#print(choices(x, k=tamanho)) generates a list of random numbers but with repetition of elements
print('-----------------------')
lista = sample(x,size) #generates a list of random numbers but without duplicates
num  = int(input('Entre com um numero: '))
 
#separates the list into two sublists :
n= 2
splited = [lista[i::n] for i in range(n)]
print(splited)

#checks whether the element belongs to the sublist

for x in splited: 
   if num in x:
       print(f'{num} :this sublist belongs')   
   else:
       print(f'{num} :this sublist does not belong')  

   print(f'{x}')      






   

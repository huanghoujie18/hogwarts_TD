#找质数
num=[]
i=2
for i in range(2,100):
   j=2
   for j in range(2,i): #相当于在i-1里面找是否能够整除i的数，如果能整除，说明不是质数。
      if(i%j==0): #因为质数除了能被1和本身整除之外，都必能被其他数整除。
         break
   else:
      num.append(i)
print(num)

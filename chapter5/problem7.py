import os  
import sys  
def split(filename,n):  
   f=open(filename,'r')  
   text=f.readlines()  
   lng=len(text)
   i=0 
   j=0  
   while i <lng:  
    fname='file%d'% j  
    print fname  
    i+=n  
    j+=1  
    index = open(os.path.join('test', fname), 'w')  
    for k in text[:n]:  
     index.write(k)  
    index.close()  
    text=text[n:]  
split(sys.argv[1],sys.argv[2])

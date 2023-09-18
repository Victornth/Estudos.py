def multi(*args):
    c = 1
    for i in args:
        c = c * i
    return c 

        
    

print(multi(2,5,7,8,9,8,7,4,5,2,4,4,4))    

def par_impar(a):
    if a%2 == 0:
        return('é par')
    else:
        return('é impar')

#print(par_impar())
print(multi(3,3,3))

 
   

################################  sorted array #############################

size_array=int(input("lotfan size araye ra vared konid : "))
araye=[]
for i in range (size_array) :
    adad=int(input("lotfan adad khod ra vared konid : "))
    araye.append(adad)
print("araye vared shode : " , araye , )     
print ("araye moratab shode : " , sorted(araye) , "\n")
if sorted(araye)==araye :
    print ("yes")    
else : 
    print ("no")        

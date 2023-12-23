################################  Non-duplicate array #############################

import random
size_array=int(input("lotfan size araye ra vared konid : "))
araye=[size_array]
for i in range (size_array) :
    adad=random.randint(0,1000)
    for i in range (len (araye)) :
        if adad not in araye :
            araye.append(adad)
print ("array : " , araye)        

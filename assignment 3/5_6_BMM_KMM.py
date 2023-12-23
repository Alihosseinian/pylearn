######################################## BMM ############################################################
def BMM(a,b):
    cc = 1
    if a > b:
        x = b
    else:
        x = a
    for i in range(x, 1, -1):
        if ((a % i == 0) and (b % i == 0)):
            cc = i
            break
    print("BMM = " , cc)
########################################## KMM ##########################################################
def KMM (a,b):
    cc = a * b
    if a < b:
        x = b
    else:
        x = a
    for i in range(x, a*b, x):
        if ((i % a == 0) and (i % b == 0)):
            cc = i
            break
    print("KMM = " , cc)
########################################## main ##########################################################
while True:
    gozine =int(input("lotfan gozine mored nazar ra entekhab konid : \n1.BMM \n2.KMM \n"))
    if gozine ==1 :
     
        adad_aval= int(input("lotfan adad aval ra vared konid :"))
        adad_dovom= int(input("lotfan adad aval ra vared konid :"))
        BMM(adad_aval , adad_dovom)  

    elif gozine ==2:
        adad_aval= int(input("lotfan adad aval ra vared konid :"))
        adad_dovom= int(input("lotfan adad aval ra vared konid :"))
        KMM(adad_aval , adad_dovom)        
        exit
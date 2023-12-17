import random

print ("** welcome**")
count_user= 0
count_comp= 0 
while True :
        
        print ("1- sang")
        print ("2- kaghaz")
        print ("3- gheichi")
        user = (int(input ("lotfn gozine mored nazar ra vared konid :")))
        while True :
                if user != 1 and user != 2 and user != 3 :
                    print ("lotfan adadi bein 1 - 3 entekhab konid 😒")
                    user = (int(input ("lotfn gozine mored nazar ra vared konid :")))
                else :
                    break
        comp = random.randint(1,3)
        if (user == 1 and comp == 1) :
            print ("har do nafar sang avordn ---> barande nadasht ")
            print ("computer :",count_comp , "&" , "user :" , count_user)
######################################################################################################
        elif (user == 2 and comp == 2) :
            print ("har do nafar kaghaz avordn ---> barande nadasht ")
            print ("computer :",count_comp , "&" , "user :" , count_user)
######################################################################################################
        elif (user == 3 and comp == 3) :
            print ("har so nafar gheichi avordn ---> barande nadasht  ")
            print ("computer :",count_comp , "&" , "user :" , count_user)  
#######################################################################################################
        elif (user == 1 and comp == 2) :
            print ("barande in round computer ast ")
            count_comp+= 1 
            print ("computer :",count_comp , "&" , "user :" , count_user) 
#######################################################################################################
        elif (user == 2 and comp == 1) :
            print ("barande in round user ast ")
            count_user+= 1 
            print ("computer :",count_comp , "&" , "user :" , count_user)
#######################################################################################################
        elif (user == 1 and comp == 3) :
            print ("barande in round user ast ")
            count_user+= 1 
            print ("computer :",count_comp , "&" , "user :" , count_user)
########################################################################################################
        elif (user == 3 and comp == 1) :
            print ("barande in round computer ast ")
            count_comp+= 1 
            print ("computer :",count_comp , "&" , "user :" , count_user)
########################################################################################################
        elif (user == 2 and comp == 3) :
            print ("barande in round computer ast ")
            count_comp+= 1 
            print ("computer :",count_comp , "&" , "user :" , count_user)  
#########################################################################################################
        elif (user == 3 and comp == 2) :
            print ("barande in round user ast ")
            count_user+= 1 
            print ("computer :",count_comp , "&" , "user :" , count_user)
#########################################################################################################
        if (count_user == 5 or count_comp == 5) :
            if (count_user > count_comp ) :
                print ("barande in bazi user ast 👏👏")
            else :
                print ("barande in bazi computer ast 👏👏 ")
            break        
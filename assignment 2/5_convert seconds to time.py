##########################################################################################
############################################# model 1 (using method ) ####################
##########################################################################################
from datetime import timedelta

sec = int (input("lotfn modat zaman ra be sanie vared konid : "))
print('Time in Seconds:', sec)

td = timedelta(seconds=sec)
print('Time in hh:mm:ss:', td)
##########################################################################################
############################################# model 2 ####################################
##########################################################################################
import math
sec_2 = int (input("(model 2 )lotfn modat zaman ra be sanie vared konid :"))
hour = sec_2 / 3600 
minutes = (sec_2 % 3600) / 60 
second = (sec_2 % 3600) / 60 
print (math.floor(hour) , ":" , math.floor(minutes) , ":" , math.floor(second) ,)
################################# convert second to hours positions #################################
saat=(input("lotfan modat zaman khod ra vared konid : (MESAL ---> 12:52:45 ) : "))
hours , minuts , second = saat.split(":")
sec=int(hours)*3600 + int(minuts)*60+ int(second)
print("modat zaman vared shode be sanie barabar ast ba :", sec)
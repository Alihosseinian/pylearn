################################  hangman #############################

import random

words_bank=['nasa' , 'mercury' , 'venus' , 'earth' , 'mars' , 'jupiter' , 'saturn' , 'uranus' , 'neptune' , 'moon']
selected_word=random.choice(words_bank)
print("kalame entekhab shodeh : ")
for i in range(len(selected_word)):
    print (" _ ",end=' ' )
print("tedad eshtebahat mojaz(joon) : 5")
joon=5
user_true_chars=" " *len(selected_word)
while True :
    for Char in selected_word:
        if Char in user_true_chars:
            print(Char,end='')
        else:
            print(" ",end='') 
            
    user_char=input("\n lotfan harf mored nazar ra vared konid : ")
    i=int(input("\n lotfan shomare mahal harf mored nazar ra vared konid : "))-1 ## barai chek kardn index harf dar kalame 
    if user_char == selected_word[i] :                                         ##yani alave bar inke bayad hrf dorost bashd bayad makan harf dar kalme ham dorost bashd 
        print("hads shoma dorost bod ✅ ")
        user_true_chars = user_true_chars [:i]+ (user_char) + user_true_chars [i+1:]
        print (user_true_chars)
    else : 
        print("hads shoma nadorost bod ❌ ")
        joon -=1 
        print("joon baghi mande : " ,joon)
    if joon==0 : 
        print("game over","kalame : ",selected_word)
        break
    if (user_true_chars ==  selected_word):
        print("game win ", "kalame hads zades shode : " ,selected_word)
        break
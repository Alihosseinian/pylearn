################################  Word counter #############################

jomle = input("jomle khod ra vared konid : ").strip() ## tabe strip() vase hazf krdn space aval v akhr jomle hast
counter = 1
for char in jomle :
    if char == ' ':
        counter += 1
print("tedad kalamat mojod dar jomle : ", counter)
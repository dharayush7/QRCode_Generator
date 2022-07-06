import qrcode
print(" ")
print("             ***** QRCode_Generator *****")
print(" ")
url = input("Enter your url or sms:")
print(" ")
qrsz,bdsz =0,0
colinp = ""
a,b,c,d=0,0,0,0
print("Select Size:")
print("1. Small")
print("2. Medium (Recomonded)")
print("3. High")
print(" ")
print(" ")
qrszinp = input ("Enter your Size no. :")
if "1" in qrszinp:
    qrsz = 10
elif "2" in qrszinp:
    qrsz = 20
elif "3" in qrszinp:
    qrsz = 40
else :
    a=1
if a==0:
    print(" ")
    print("Select Border Size:")
    print("1. Narrow")
    print("2. Medium (Recomonded)")
    print("3. High")
    bdszinp = input(" Enter your Border Size: ")
    if "1" in bdszinp:
        bdsz = int(2)
    elif "2" in bdszinp:
        bdsz = int(5)
    elif "3" in bdszinp:
        bdsz = int(10)
    else:
        b = 1
        
else:
    pass

if a==0 and b==0:
    print(" ")
    print("Select QRCode Color:")
    print("1. Black")
    print("2. Red")
    print("3. Blue")
    print("4. Yellow")
    print("5. Green")
    print(" ")
    colinp = input("Enter Color no. :")
    if "1" in colinp :
        col = "Black"
    elif "2" in colinp:
        col = "Red"
    elif "3" in colinp:
        col = "Blue"
    elif "4" in colinp:
        col = "Yellow"
    elif "5" in colinp:
        col = "Green"
    else:
        c = 1

else:
    pass

if a==0 and b==0 and c==0:
    print(" ")
    name=input("Give a name of thise qrcode :")
    if len(name)==0:
        d = 1
    else:
        pass
    
else:
    pass

if a==0 and b==0 and c==0 and d==0:

    qr = qrcode.QRCode(version=1,
                    error_correction = qrcode.constants.ERROR_CORRECT_H,
                    box_size = qrsz,border = bdsz,)
    qr.add_data(url)
    qr.make(fit = True)
    img = qr.make_image(fill_color= col)
    img.save(name+"_qrcode.png")
    print(" ")
    print ("your QRCode save as " + name +"_qrcode.png")
    print(" ")
else :
    pass
if a==1 or b==1 or c==1:
    print(" ")
    print("invalid input!")
    print(" ")
else:
    pass


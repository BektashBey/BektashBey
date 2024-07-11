vize1 = int(input("vize1 notu gir: "))
vize2 = int(input("vize2 notu gir: "))
final = int(input("final notu gir: "))

not_ort = vize1 * 3/10 + vize2 * 3/10 + final * 4/10 

if(not_ort >= 90):
    print("AA")
elif(not_ort >= 85):
    print("BA")    
elif(not_ort >= 80):
    print("BB")
elif(not_ort >= 75):
    print("BC")
elif(not_ort >= 70):
    print("CC") 
elif(not_ort >= 65):
    print("CD")
elif(not_ort >= 60):
    print("DD") 
elif(not_ort >= 55):
    print("FD") 
else:
    print("FF")

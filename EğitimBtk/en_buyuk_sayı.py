a = int(input("sayı giriniz:"))

b = int(input("sayı giriniz:"))

c = int(input("sayı giriniz:"))

if( a >= b and a >= c ):
    print("en büyük sayı" , a)

elif( b >= a and b >= c ):
    print("en büyük sayı" , b)

elif( c >= a and c >= c ):
    print("en büyük sayı" , c)
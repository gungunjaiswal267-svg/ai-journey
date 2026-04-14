# program is showing marks and grades using if/else

marks = float(input("ENTER YOUR MARKS:"))

print("="*10)
print("MARKS:",marks)

if marks>=95 :
    
    print("GRADE:A+")
    print("STATUS:You are doing fabulous")

elif marks>=80 :
    
    print("GRADE:A")
    print("STATUS:You are doing excellent")

elif marks>=70 :
    
    print("GRADE:B+")
    print("STATUS:You are doing good")

elif marks>=60 :
    
    print("GRADE:B")
    print("STATUS:You are doing good")

elif marks>=45 :
    
    print("GRADE:C")
    print("STATUS:You are doing good,but can do better ")

elif 0>marks>100 :
    print("Invalid,please enter number between 0 to 100")
    
    
else :
    
    print("GRADE:f")
    print("STATUS:Need to work hard")   

print("="*10)

    


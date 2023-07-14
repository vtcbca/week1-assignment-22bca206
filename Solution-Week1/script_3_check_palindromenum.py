#Write A Script TO Check Number Is Palindrome Or Not
def check_palindromeno(num):
    if num.isdigit() == True:
        num=int(num)
        cp=num
        re=0
        while(num>0):
            d=num%10
            re=re*10+d
            num=num//10
        if re == cp:
            print("Number Is Palindrome")
        else:
            print("Number Is Not Palindrome")
    else:
        print("\n\t Inputted Number Is Not In Integer ...\n\t Please Enter Valid Number")
num=input("Enter Any Number :")
check_palindromeno(num)

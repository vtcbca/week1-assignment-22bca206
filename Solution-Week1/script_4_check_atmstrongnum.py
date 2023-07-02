#Write A Script To Check Armstrong Number Or Not
def check_armstrongno(num):
    if num.isdigit() == True:
        num=int(num)
        cp=num
        sum=0
        while(num>0):
            d=num%10
            re=d*d*d
            sum=sum+re
            num=num//10
        if cp==sum:
            print(f"{cp} Is Armstrong Number!")
        else:
            print(f"{cp} Is Not Armstrong Number!")
    else:
        print("\n\t Inputted Number Is Not A Integer ...\n\t Please Enter Valid Number")
num=input("Enter Any Number:")
check_armstrongno(num)

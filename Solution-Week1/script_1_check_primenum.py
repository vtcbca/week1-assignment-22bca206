#Python Script To Check Number Is Prime Or Not
def check_primeno(no):
    for i in range(2,no):
        if no%i==0:
            print(f'{no} Is Not Prime Number')
            break
    else:
        print(f'{no} Is Prime Number')
no=int(input("Enter Any Number:"))
check_primeno(no)

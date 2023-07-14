# Write A Script To Print Sum OF Its Digit
def sum_of_digit(num):
    sum=0
    while(num>0):
        d=num%10
        sum=sum+d
        num=num//10
    print(f'Sum Is : {sum}')
num=int(input("Enter Any Number :"))
sum_of_digit(num)

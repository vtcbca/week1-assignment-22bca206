#Write A Script To Print Index Value Instead of Printing Vowels In String
def print_indexval(string):
    vowels=['a','e','i','o','u','A','E','I','O','U']
    cpstr=[]
    sep=' '
    for i in range(0,len(string)):
        if string[i] in vowels:
            cpstr.append(str(i))
        else:
            cpstr.append(string[i])
    result=sep.join(cpstr)
    print(f"\n\t Inputted String Is :- {string} \n\t After Updating String Is :- {result}")
string=input("\nEnter Any String :")
print_indexval(string)

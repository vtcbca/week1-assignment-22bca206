#Write A Script To Enter Any String And Count Vowels
def count_vowels(string):
    a=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for i in string:
        if i in vowels:
            a+=1
    print(f"Vowels In String Are {a}")
string=input("\n Which String You'r Gonna Enter ...? :")
count_vowels(string)

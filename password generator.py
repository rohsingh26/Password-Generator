import random
import string

def passwrd(ln):
    l = string.ascii_letters
    d = string.digits
    s = string.punctuation
    ac = l + d + s
    st = ("")
    for i in range(ln):
        n = random.choice(ac)
        st = st + n
    return st

def main():
    n=int(input("Enter the number of people for which you want the password= "))
    t=int(input("Enter the length of password you want= "))
    for i in range(1,n+1):
        x=passwrd(t)
        print(f"Password for Person_{i} = {x}")

if __name__=="__main__":
    main()

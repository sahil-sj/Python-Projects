#Email Validation using string functions
import string

k=0;j=0;d=0
email=input("Enter your email : ") #g@g.in (minimum 6 chracters)
if len(email)>=6:#1. length should be greater than or equal to 6
    if email[0].isalpha:#2. first letter should be letter
        if "@" in email and (email.count("@")==1):#3. @ should present and only 1 time 
            if ((email[-3] == '.') ^ (email[-4]=='.')):#4. Xor is used bcz . is reqd only in one position 
                for i in email: #5. for space checking we have to iterate whole string
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                    print("Uppercase letters are not allowed or use only '_' as a special chracter ")
                else:
                    print("Right email")
            else:
                print(". is requred at last 3rd or last 4th position")
        else:
            print("@ is required one's")
    else:
        print("Ist position should be alphabet")
else:
    print("Length should be greater than 6.")

k
import time


f = open("dictionary.txt","r")

print("Can your password survive a dictionary attack?")

#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")

print(test_password + "?")
time.sleep(0.7)

fd=f.read()
test_password=test_password.strip()


if(test_password in fd):
    print("Weak")
    
if( test_password not in fd):
    print("thats alright")

    #.upper
    #.lower
        



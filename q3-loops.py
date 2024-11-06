#Accept a number n from the user and print its multiplication table

n = int(input("Enter a number"))

for i in range(10):
    print(n,"X",i,"=",n*i)
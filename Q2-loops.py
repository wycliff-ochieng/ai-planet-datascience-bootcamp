#Iterate over the following list and print the elements:
#list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

list1 = [12,15,32,42,55,75,122,132,150,180,200]

for item in list1:
    print(item)

#OR

for index,item in enumerate(list1):
    print(f"Index:{index},Item:{item}")

name_list = []
name = input("Please enter the name: ")

while name.lower() != 'stop':
    name_list.append(name)
    name = input("Please enter the name: ")

for name in name_list:
    print(name)

print("done with printing out the names.")


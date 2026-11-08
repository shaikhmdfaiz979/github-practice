import os

folders = input("Please enter the folders name using space between them like (/opt /tmp): ").split(" ")

for folder in folders:
    try: 
        files = os.listdir(folder)
    except FileNotFoundError:
        print(f"Looks like '{folder}' doesn't exist")
        continue
    except PermissionError:
        print(f"Looks like you don't have permission to acccess")
        continue
    print("=== listing files for the folder: "+ folder)
    for file in files:
        print(file)
        
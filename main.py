import filecmp
import os
x = 0
all_files = os.listdir()
file_name_1 = input("What\'s the file name?")
if file_name_1 in all_files:
    all_files.remove(file_name_1)
else:
    print("That file doesn\'t exist.")

for files in all_files:
    while file_name_1 in all_files:
        all_files.remove(file_name_1)
    try:
        answer = filecmp.cmp(file_name_1, files)
    except:
        print("I can\'t check duplicates for that file type, sorry.")
    if answer is True:
        os.remove(files)
        print(f"{files} is a duplicate. Deleting")
        x + 1
    else:
        if x == 0:
            pass
        elif x > 0:
            print(f"Finished deleting {str(x)} duplicates of {file_name_1}")

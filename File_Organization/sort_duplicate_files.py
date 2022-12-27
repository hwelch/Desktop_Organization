import os

# python script to organize all duplicate files into a folder called duplicates

# read in the file directory we are sorting from the user
parent_dir = input("Enter Directory you want to sort: ")

# setting up the correct directory for os module
os.chdir(parent_dir)
files = os.listdir()

# first we will make the directory to store duplicates if it does not already exist
duplicate_dir = 'duplicates'
duplicate_path = os.path.join(parent_dir, duplicate_dir)

if duplicate_dir not in files:
    os.mkdir(duplicate_path)
    print(f"Directory {duplicate_path} added")
else:
    print(f"Directory {duplicate_path} already existed")


# next we will iterate through the files in the directory and move duplicates to the proper location

# function to change the directory of a given file
def change_dir(file, new_dir):
    old_path = os.path.join(parent_dir, file)
    new_path = os.path.join(new_dir, file)
    os.rename(old_path, new_path)


# function to check if a file is a duplicate
# a file is a duplicate if it has (version number).filetype at the end of the file
# function returns true if it is a duplicate otherwise false
def is_duplicate(file):
    index_left_par = file.find('(')
    # right par will have a . after it because it is at the end of the file name the parenthesis appears for duplicates
    index_right_par = file.find(').')
    if(index_left_par != -1 and index_right_par != -1):
        return True
    else:
        return False


count = 0
for file in files:
    if file != 'duplicates' and is_duplicate(file):
        change_dir(file, duplicate_path)
        count += 1

print(f'Moved {count} duplicates.')
import os

# python script to organize files in a dirrectory
# places the .pdf, .txt, and .docx files in one folder and all other types in another


# read in the file directory we are sorting from the user
parent_dir = input("Enter Directory you want to sort: ")

# first we will make the two directories to store everything if the folders to not already exist
os.chdir(parent_dir)
files = os.listdir()

text_files_dir = 'text_files'
other_dir = 'other'

text_path = os.path.join(parent_dir, text_files_dir)
other_path = os.path.join(parent_dir, other_dir)

if text_files_dir not in files:
    os.mkdir(text_path)
    print(f"Directory {text_path} added")
else:
    print(f"Directory {text_path} already existed")

if other_dir not in files:
    os.mkdir(other_path)
    print(f"Directory {other_path} added")
else:
    print(f"Directory {other_path} already existed")


# function to change the directory of a given file
def change_dir(file, new_dir):
    old_path = os.path.join(parent_dir, file)
    new_path = os.path.join(new_dir, file)
    os.rename(old_path, new_path)


count = 0
# next we will loop through all of the files in the parent directory 
# and sort them into the two directories (text_files and other)
for file in files:
    if file != 'text_files' and file != 'other':
        if '.pdf' in file or '.txt' in file or '.doc' in file:
            change_dir(file, text_path)
        else:
            change_dir(file, other_path)
        count += 1

print(f'Organized {count} files')
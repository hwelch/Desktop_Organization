import os

# python script to organize files in a dirrectory
# places the .pdf, .txt, and .docx files in one folder and all other types in another


# read in the file directory we are sorting from the user
parent_dir = input("Enter Directory you want to sort: ")

# first we will make the two files to store everything if they are not already made
os.chdir(parent_dir)
files = os.listdir()

text_files_dir = 'text_files'
other_dir = 'other'

text_path = os.path.join(parent_dir, text_files_dir)
other_path = os.path.join(parent_dir, other_dir)

if text_files_dir not in files and other_dir not in files:
    os.mkdir(text_path)
    os.mkdir(other_path)
    print("Directories {text_path} and {other_path} added")
else:
    print("Directories {text_path} and {other_path} already existed")


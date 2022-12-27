import os

# exit the current folder
def pop_out(dir):
    split_filename = (str(dir)).split('\\')
    new_filename = ''
    i = 0
    while i < len(split_filename) - 1:
        new_filename += (split_filename[i] + '\\')
        i += 1
    return new_filename

# get the current directory
current_dir = os.getcwd()
print(os.listdir())
print("DIR:", current_dir)

# change directory
new_file_path = pop_out(current_dir)
print("path:", new_file_path)
os.chdir(new_file_path)
new_dir = os.getcwd()
print("NEW DIR:", new_dir)

# get list of internal files and folders
l = os.listdir()
print(l)

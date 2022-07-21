import os
import shutil

from_dir = "C:\Users\DELL\Downloads"
to_dir ="C:\Users\DELL\Documents\Document_Files"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.spiltext(file_name)
    
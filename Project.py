import os
import shutil

from_dir = "C:\\Users\\Envy\Desktop\\Images111"
to_dir = "C:\\Users\Envy\\Desktop\\test"
os.path.exists(from_dir)
list_of_files = os.listdir(from_dir)
print(list_of_files)

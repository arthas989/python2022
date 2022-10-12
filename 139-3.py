# 139-3.py
# shutil zip folder
import shutil

folder_we_want_to_zip = "C:\\Users\\user\\Desktop\\python\\python2022\\Employee"
output_name = "C:\\Users\\user\\Desktop\\python\\python2022\\output"

shutil.make_archive(output_name, "zip", folder_we_want_to_zip)

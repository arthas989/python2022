# 139-4.py
# shutil unzip

import shutil

something_we_want_to_unzip = "C:\\Users\\user\\Desktop\\python\\python2022\\output.zip"
unzipped_folder_name = "C:\\Users\\user\\Desktop\\python\\python2022\\shutil_result"

shutil.unpack_archive(something_we_want_to_unzip, unzipped_folder_name, "zip")

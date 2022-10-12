# 139-2.py
# unzip
import zipfile

zipped_obj = zipfile.ZipFile("research.zip", "r")
zipped_obj.extractall("result")
zipped_obj.close()

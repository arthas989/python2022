# 139-5.py
# pyzipper can read and write AES encrypted zip files

# TERMINAL pip install pyzipper

import pyzipper
secret_password = b'123456'

with pyzipper.AESZipFile('new_test.zip',
                         'w',
                         compression=pyzipper.ZIP_LZMA,
                         encryption=pyzipper.WZ_AES) as zf:
    zf.setpassword(secret_password)
    zf.setencryption(pyzipper.WZ_AES, nbits=256)
    zf.write("research.txt")
    ## zf.writestr('test.txt', "What ever you do, don't tell anyone!")

with pyzipper.AESZipFile('new_test.zip') as zf:
    zf.setpassword(secret_password)
    zf.extractall("result")
    ## my_secrets = zf.read('test.txt')
    # print(my_secrets)

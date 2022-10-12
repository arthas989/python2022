# 138-2.py
# 找出文字檔中全部的inline-citation
# (alphanumeric space, number >= 4)

import re
with open("research.txt", encoding="utf8") as f:
    text = f.read()
    x = re.findall(r"\([A-Za-z0-9\s]+, \d{4,}\)", text)
    print(x)

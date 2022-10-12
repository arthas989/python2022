import re
text = 'a b c,abc,a\nb\nc,a    b    c'
match = re.findall(r'a\s{4}b\s{4}c', text)
print(match)

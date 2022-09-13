# iterable => (1) __iter__()method returns an iterator
# any generator is an iterator
class Something:
    def __iter__(self):
        yield 5
        for x in range(1, 4):
            yield x


s = Something()
# s is an iterable
# iter(iterable) returns an iterator
print(iter(s))
for i in s:
    print(i)

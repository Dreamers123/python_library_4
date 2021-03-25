from fnmatch import fnmatchcase as match

addresses = [
    '5462 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '1022 N CLARK AVE',
    '4802 N BROADWAY',
]

a = [addr for addr in addresses if match(addr, '* ST')]
print(a)

b = [addr for addr in addresses if match(addr, '54[2-9][0-9] *ST*') or match(addr, '10[2-9][0-9] *AVE*') ]
print(b)
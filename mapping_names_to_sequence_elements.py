from collections import namedtuple

Stock = namedtuple('Stock', ['name', 'shares', 'price','profit'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += (s.shares * s.price)+s.profit
    return total

# Some Data
records = [
    ('GOOG', 100, 490.1,10),
    ('ACME', 100, 123.45,20),
    ('IBM', 50, 91.15,9)
]

print(compute_cost(records))
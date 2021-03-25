records = [
     ('foo', 1, 2),
     ('bar', 'hello'),
     ('Test', {'Far':'Way', 'Home':'Town'}),
]

def do_foo(x,y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)
def do_Kar(s):
    for key,value in s.items():
        print('Test', value)
for tag, *args,  in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
    else:
        do_Kar(*args)
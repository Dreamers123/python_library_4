# def myFun(arg1, arg2, arg3,Abeer):
#     print("arg1:", arg1)
#     print("arg2:", arg2)
#     print("arg3:", arg3)
#     print("arg4:", Abeer)
#
# # Now we can use *args or **kwargs to
# # pass arguments to this function :
# args = ("Geeks", "for", "Geeks","Test")
# myFun(*args)
#
# kwargs = {"arg1": "Geeks", "arg2": "for", "arg3": "Geeks", "Abeer":"Tanzila"}
# myFun(**kwargs)

def myFun(*args, **kwargs):
    print(args)
    for key,value in kwargs.items():
        print( key +' : '+value)


# Now we can use both *args ,**kwargs
# to pass arguments to this function :
myFun('geeks', 'for', 'geeks', first="Geeks", mid="for", last="Geeks")
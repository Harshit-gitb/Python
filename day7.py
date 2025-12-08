# function 
def greet():
    print("hello!")
    print("how are u?")


greet()


def greet_name(name):
    print(f"Hello {name}")


greet_name("hc")


def greetWithKeyword(fn,ln):
    print(f"hello {fn} {ln}")


greetWithKeyword(fn="jack",ln="danny" )
greetWithKeyword("the",ln="rock")


# Return the value

def square_number(n):
    return n*n 
    

result = square_number(3)
print(result)


x = 10  # Global variable

def modify():
    global x
    x += 5

modify()
print(x)  # Output: 15


x = 4

##Define the function
def insideX():
    global x
    x = 17
    print("Value X inside the function is a local variable of: ", x)
##Execute the function
insideX()
print("Value X outside the function is a global variable of: ", x)

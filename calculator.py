import re

print("Aliyah's Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def do_math():
    global run
    global previous
    equation = ""
    
    # A previous prompt is used 
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    # If the user quits
    if equation == "quit":
        print("Goodbye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.()" "]', ' ', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    do_math()

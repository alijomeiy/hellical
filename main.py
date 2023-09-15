NUMBERS = "1234567890"

def calculate(expression):
    first_number = 0
    seconde_number = 0
    operator = ""
    for c in expression:
        if c in NUMBERS: # also possible c.isdigit()
            if operator == "":
                first_number *= 10
                first_number += int(c)
            else:
                seconde_number *= 10
                seconde_number += int(c)
        else:
            operator = c
    if operator == "+":
        return first_number + seconde_number
    return "Error"

done = False

while not done:
    user_input = input(">>> ")
    if user_input == "exit":
        done = True
    else:
        result = calculate(user_input)
        print(result)
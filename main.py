NUMBERS = "1234567890"
OPERATIONS = "x/+-"


def calculate(expression):
    result = expression
    while have_strings_any_common_characters(expression, OPERATIONS):
        highest_priority_expression = get_higest_priority_operation(expression)
        result = calculate_simple_expression(highest_priority_expression)
        expression = expression.replace(highest_priority_expression, str(result))
    return result


def get_higest_priority_operation(expression):
    index = len(expression)
    flag = False
    if "x" in expression:
        index = expression.index("x")
        flag = True
    if "/" in expression:
        substraction_index = expression.index("/")
        if substraction_index < index:
            return get_expression_around(substraction_index, expression)
        if flag:
            return get_expression_around(index, expression)

    if "+" in expression:
        index = expression.index("+")
        flag = True
    if "-" in expression:
        substraction_index = expression.index("-")
        if substraction_index < index:
            return get_expression_around(substraction_index, expression)
        if flag:
            return get_expression_around(index, expression)


def get_expression_around(index, expression):
    start_index = find_operation_previous_number_start_index(index, expression)
    end_index = find_operation_next_number_end_index(index, expression)
    return expression[start_index, end_index]


def find_operation_previous_number_start_index(index, expression):
    pointer = index - 1
    while pointer >= 0 and expression[pointer] in NUMBERS:
        pointer -= 1
    return pointer


def find_operation_next_number_end_index(index, expression):
    pointer = index + 1
    while pointer < len(expression) and expression[pointer] in NUMBERS:
        pointer += 1
    return pointer


def have_strings_any_common_characters(string1, string2):
    for ch in string1:
        if ch in string2:
            return True
    return False


def calculate_simple_expression(simple_expression):
    return 0


done = False

while not done:
    user_input = input(">>> ")
    if user_input == "exit":
        done = True
    else:
        result = calculate(user_input)
        print(result)

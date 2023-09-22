NUMBERS = "1234567890"
OPERATORS = "x/+-"  # In order of priority


def calculate(expression):
    while have_strings_any_common_characters(expression, OPERATORS):
        highest_priority_expression = get_expression_around_operator(expression,
                                                                     get_highest_priority_operator_index(expression))
        result = calculate_simple_expression(highest_priority_expression)
        expression = expression.replace(highest_priority_expression, str(result))
    return expression


def get_highest_priority_operator_index(expression):
    for operator in OPERATORS:
        if operator in expression:
            return expression.index(operator)


def get_expression_around_operator(expression, index):
    start = find_previous_number_start_index(expression, index)
    end = find_next_number_end_index(expression, index)

    return expression[start:end]


def find_previous_number_start_index(expression, index):
    pointer = index - 1
    while pointer > 0 and expression[pointer] in NUMBERS:
        pointer -= 1
    return pointer


def find_next_number_end_index(expression, index):
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
    # TODO
    return 0


done = False
while not done:
    user_input = input(">>> ")
    if user_input == "exit":
        done = True
    else:
        result = calculate(user_input)
        print(result)

def add_two_numbers() -> int:
    user_input = input()
    list_of_number = user_input.split(",")
    return sum(list(map(int, list_of_number)))



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())

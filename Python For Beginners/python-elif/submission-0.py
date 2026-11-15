def check_range(num: int) -> str:
    result = ""
    if num < 0:
        result = "negative"
    elif num == 0:
        result = "zero"
    elif num < 10:
        result = "positive single digit"
    else:
        result = "positive multi digit"
    return result







  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))

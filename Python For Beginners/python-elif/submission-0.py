def check_range(num: int) -> str:
    if num < 0:
        text = "negative"
    elif num == 0:
        text = "zero"
    elif num < 10:
        text = "positive single digit"
    else:
        text = "positive multi digit"
    return text






  
# don't modify code below this line
print(check_range(-10))
print(check_range(0))
print(check_range(9))
print(check_range(1000))

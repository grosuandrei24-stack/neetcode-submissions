def divide_numbers(a: str, b: str) -> None:
    try:
        a = int(a)
        b = int(b)
        rezultat = a/b
        print(rezultat)
    except Exception as e:
        print(f"An error occurred: {e}")



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")

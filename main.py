print("Лабораторна робота №3 Варіант 3")

print("Гліб Кобрин, ІКСМ-1, Навчальна Група №2")

while True:
    user_input = input("Введіть довільне ціле число у форматі *****: ")
    symbol = input("Введіть символ, який ви хочете бачити у гістограмі: ")

    if user_input.isdigit():

        digits = [int(digit) for digit in user_input]

        max_digit = max(digits)

        print(" ".join(map(str, digits)))

        print("_" * (len(digits) * 2))

        for i in range(max_digit, 0, -1):
            row = ""
            for digit in digits:
                if digit >= i:
                    row += symbol + " "
                else:
                    row += "  "
            print(row)

        break
    else:
        print("Error: Введене значення не є цілим числом.")

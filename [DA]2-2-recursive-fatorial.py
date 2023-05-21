def fatorial(number):
    if number == 0:
        return 1
    else:
        result = fatorial(number - 1)
        return result * number

print(fatorial(4))
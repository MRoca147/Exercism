def is_armstrong_number(number):
    order = len(str(number))
    temp = number
    suma = 0
    while temp > 0:
        digit = temp % 10
        suma += digit ** order
        temp //= 10
    
    if suma == number:
        return True
    else:
        return False

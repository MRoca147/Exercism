def prime(number):
    try:
        if number == 0:
            int("string")
    except ValueError:
        raise ValueError("ValueError exception thrown")
    primes = [2]
    p = 3
    while len(primes) < number:
        for i in primes:
            if p%i == 0:
                break
        else:
            primes.append(p)
        p += 2
    return primes[-1]

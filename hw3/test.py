def factorize(*numbers):
    result = []
    for number in numbers:
        factors = [i for i in range(1, number + 1) if number % i == 0]
        result.append(factors)
    return result

a, b, c, d = factorize(128, 255, 99999, 10651060)
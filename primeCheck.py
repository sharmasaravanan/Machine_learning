def isPrime(num):
    """
    This function is to return the prime check flag for the given number
    """
    flag = True
    for i in range(2, num):
        if num % i == 0:
            flag = False
    return flag

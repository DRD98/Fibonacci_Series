def fibonacci(number):

    if number <= 0:
        print("Nothing to print")
        return
    
    first, second = 0, 1

    fib_series = [str(first), str(second)] if number > 1 else [str(first)]
    
    for _ in range(number - 2):
        first, second = second, first + second
        fib_series.append(str(second))
    
    print("The Fibonacci Series is:\n" + "\t".join(fib_series))

number = int(input("Enter a number: "))
fibonacci(number)
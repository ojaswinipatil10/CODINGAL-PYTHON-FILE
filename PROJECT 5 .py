def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\033[1;35m🌸 Fibonacci Sequence 🌸\033[0m")

terms = int(input("\033[1;36mEnter the number of terms: \033[0m"))

print("\n\033[1;32mSequence:\033[0m")

for i in range(terms):
    print("\033[1;33m", fibonacci(i), end=" ")
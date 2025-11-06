def fib_rec(n):
    global r_steps
    r_steps += 1
    return n if n <= 1 else fib_rec(n-1) + fib_rec(n-2)

def fib_iter(n):
    global i_steps
    a, b = 0, 1
    print("Iterative:", end=" ")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
        i_steps += 3
    print()

r_steps = i_steps = 0
n = int(input("Enter n: "))

print("Recursive:", end=" ")
for i in range(n):
    print(fib_rec(i), end=" ")
print("\nRecursive Steps:", r_steps)

fib_iter(n)
print("Iterative Steps:", i_steps)

celsius_to_fahrenheit = lambda c: c * 9/5 + 32

is_even = lambda n: n % 2 == 0

# prof solution
def celsius_to_fahrenheit(c_temp: float) -> float:
    """Return the fahrenheit equivalent of the celsius temperature provided.
    """
    return 9 * c_temp / 5 + 32

if __name__ == "__main__":
    print(celsius_to_fahrenheit(0))

"""
with open("is_even.py", "w") as file:
    file.write("n = int(input('enter a number: '))\n")
    for i in range(10000):
        file.write(f"if n == {i}:\n")
        file.write(f"  print('{'even' if i % 2 == 0 else 'odd'}')\n")
"""

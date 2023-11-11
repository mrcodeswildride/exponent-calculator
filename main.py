print()

base = int(input("Enter the base: "))
power = int(input("Enter the power: "))
product = 1

if power > 0:
  print()

for n in range(power):
  product = product * base
  print(f"Iteration {n+1} product: {product:,}")

print(f"\n{base} to the power of {power} is {product:,}.")

"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
  # Step 1
  if number_of_primes <= 0:
    raise ValueError("The number of primes must be a positive integer.")

  # Step 2
  list = []
  num = 2

  # Step 3
  while len(list) < number_of_primes:
    # Step 3a
    for prime in list:
      if num % prime == 0:
        break
    else:
      list.append(num)

    # Step 3b
    num += 1

  # Step 4
  return list
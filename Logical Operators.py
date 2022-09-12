is_magician = True
is_expert = False

# Checks if Magician and Expert: Prints "You are a master magician"
if is_magician and is_expert:
  print("You are a master magician.")

# Checks if Magician but not Expert: Prints "At least you're getting there"
elif is_magician and not is_expert:
  print("At least you're getting there.")

# Checks if not a Magician: Prints "You need magic powers."
elif not is_magician:
  print("You need magic powers.")

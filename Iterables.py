user = {
  'name': 'Golem',
  'age': 5006,
  'can_swim': False
}

for item in user.items():
  print(item) # Will return key value pairs as a tuple in console.

for item in user.values():
  print(item) # Will return just the values provided.

for item in user.keys():
  print(item) # Will return name, age, and can_swim but not values.

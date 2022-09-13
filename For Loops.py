for item in 'Zero to Mastery':
  print(item) # Prints Zero to Mastery one at a time.

# For Loops run through all iterables stored in the machine memory including lists and tuples as shown below.

for item in [1,2,3,4,5]: #List shown as a For Loop example.
  print(item)

for item in (1,2,3,4,5): #Tuple shown as a For Loop example.
  print(item)

# For Loops can also be printed more than once and it will print multiple of the same iterable stored in memory, shown below.

for item in 'Zero to Mastery':
  print(item)
  print(item)
  print(item) #Prints ZZZEEERRROOO TTTOOO ..., so forth!

# You can also write nested For Loops like this:
for item in (1,2,3,4,5):
  for x in ['a','b','c']:
    print(item, x) #Prints '1 a', '1 b', '1 c', so forth!

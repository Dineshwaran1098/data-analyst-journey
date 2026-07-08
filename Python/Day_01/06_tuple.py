
fixed_coordinates = (13.0827, 80.2707) # Chennai Lat-Long (Maatha koodadhu)
print(type(fixed_coordinates)) # Output: <class 'tuple'>

fake_tuple = (5)   # Type: <class 'int'>
print(type(fake_tuple))
real_tuple = (5,)  # Type: <class 'tuple'> (Super mukkiyam!)
print(type(real_tuple))

# A tuple containing an integer and a mutable list object
tricky_tuple = (2026, [10, 20])

# Try to modify the list INSIDE the tuple:
tricky_tuple[1].append(30)

print(tricky_tuple) # Output: (2026, [10, 20, 30]) -> 
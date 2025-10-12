def squares(length):
  for n in range(length):
    yield n ** 2

for square in squares(5):
  print(square)
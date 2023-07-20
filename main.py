print('Math Game!')
print()
a = int(input('Name your multiples: '))
print()
n = 0
for i in range(1,11):
  print()
  b = i * a
  c = int(input(f'{i} X {a} = '))
  if c == b:
    print('Awesome! you got it')
    n += 1
  else:
    print(f'Nope! the correct answer is {b}')
print()
print(f'You scored {n}/10')
print()
print('See you next time')

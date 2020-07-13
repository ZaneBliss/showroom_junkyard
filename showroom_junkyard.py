showroom = set()

showroom = { 'Honda Civic', 'Toyota Prius', 'Tesla Model-X', 'Honda CR-V' }
print(len(showroom))
showroom.add('Honda Civic')
# print(showroom)
cars = ('Ford Focus', 'Spycar')
showroom.update(cars)
# print(showroom)
showroom.discard('Honda Civic')
print(showroom)

junkyard = {'Toyota Corolla', 'Ford Focus', 'Spycar'}
print(showroom.intersection(junkyard))
showroom.union(junkyard)

new_showroom = showroom.union(junkyard)
# print(new_showroom)
new_showroom.discard('Spycar')
print(new_showroom)
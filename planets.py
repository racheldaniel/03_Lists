planet_list = ['Mercury', 'Mars']

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append('Jupiter')
planet_list.append('Saturn')

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(['Uranus', 'Neptune'])

# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, 'Earth')
planet_list.insert(1, 'Venus')

# Use append() again to add Pluto to the end of the list.
planet_list.append('Pluto')

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets.
rocky_planets = planet_list[0:4]

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del(planet_list[-1])
print(planet_list)


# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Saturn')).
missions = [('Mariner 2', 'Venus'), ('Mariner 4', 'Mars'), ('Pioneer 10', 'Jupiter'), ('Pioneer 11', 'Saturn'), ('Voyager 1', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'), ('Voyager 2', 'Neptune', 'Uranus')]

# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which satellites have visited it.
for planet in planet_list:
  planet_satellite = []
  for mission in missions:
    if planet in mission:
      planet_satellite.append(mission[0])
  planets = (', ').join(planet_satellite)
  print(f'{planet} has been visited by {planets}')
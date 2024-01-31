# Messy and not that optimal, but it worked.

orbits_count = dict()
def get_orbit_count(orbits, planet):
  if planet not in orbits_count:
    planets_being_orbited = []
    try:
      planets_being_orbited = orbits[planet]
    except KeyError:
      pass
    this_planets_orbit_count = len(planets_being_orbited)
    for orbitee in planets_being_orbited:
      this_planets_orbit_count += get_orbit_count(orbits, orbitee)
    orbits_count[planet] = this_planets_orbit_count
  return orbits_count[planet]

def insert_into_graph(graph, left, right):
    try:
      graph[right].append(left)
    except KeyError:
      graph[right] = [left]

def find_path_to_root(graph, planet, root):
  path = [planet]
  if planet == root:
    return path

  for orbitee in graph[planet]:
    new_path = find_path_to_root(graph, orbitee, root)
    if new_path:
      path.extend(new_path)
      break

  if path:
    return path
  else:
    return None

def count_traverses(filepath):
  graph = dict(list())
  planets = dict()
  orbitees = dict()
  orbiters = dict()
  with open(filepath, "r") as f:
    for line in f.readlines():
      left, right = line.strip().split(")")
      insert_into_graph(graph, left, right)

      if left not in orbiters:
        orbitees[left] = True

      orbiters[right] = True
      orbitees[right] = False

      #print(orbitees)

  root_planet = None
  for planet, value in orbitees.iteritems():
    if value:
      root_planet = planet
      #print("Root: %s" % planet)

  #print(graph)

  you_path = find_path_to_root(graph, "YOU", root_planet)
  #print(you_path)
  san_path = find_path_to_root(graph, "SAN", root_planet)
  #print(san_path)

  you_dict = {planet: index for index, planet in enumerate(you_path)}
  san_dict = {planet: index for index, planet in enumerate(san_path)}
  nearest_common_planet = None
  for planet in san_path:
    if planet in you_dict:
      if not nearest_common_planet:
        nearest_common_planet = planet
        continue
      if you_dict[planet] < you_dict[nearest_common_planet]:
        nearest_common_planet = planet

  count = -2
  for planet in you_path:
    if planet == nearest_common_planet:
      break
    count += 1

  for planet in san_path:
    if planet == nearest_common_planet:
      break
    count += 1

  print("Traversal count: %s" % count)

count_traverses("6_input2.txt")

def count_orbits(filepath):
  flipped_graph = dict(list())
  with open(filepath, "r") as f:
    for line in f.readlines():
      left, right = line.strip().split(")")

      try:
        flipped_graph[right].append(left)
      except KeyError:
        flipped_graph[right] = [left]

  #print(flipped_graph)

  total_orbit_count = 0 
  for planet, _ in flipped_graph.iteritems():
    total_orbit_count += get_orbit_count(flipped_graph, planet)
  print("total_orbit_count: %d" % total_orbit_count)

count_orbits("6_input.txt")

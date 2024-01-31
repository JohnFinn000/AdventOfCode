import math                                                                              

def calc_fuel(mass):
  fuel = math.floor(mass/3) - 2 
  print("Mass: %d\tFuel: %d" % (mass, fuel))
  return fuel

def calc_all_modules(filepath):
  total_fuel = 0 
  with open(filepath, "r") as f:
    for line in f.readlines():
      line = line.strip()
      mass = int(line)
      total_fuel += calc_fuel(mass)


fuel_requirements = calc_all_modules("1_input.txt")
print("Total fuel requirements: %s" % fuel_requirements)

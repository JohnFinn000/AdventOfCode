
def calc_1(data):
  g = 0
  e = 0
  a = 0
  
  for i in range(0, len(data[0])):
    if sum([1 for d in data if (int(d, 2) >> i) & 1]) >= len(data)/2:
      a |= (1 << i)
    print "bin g " + bin(g)
    one_count = 0
    for d in data:
       if d[i] == "1":
          one_count += 1
    print one_count
    e <<= 1
    g <<= 1
    if one_count >= len(data)/2:
      g |= 1
    else:
      e |= 1
  print bin(g)
  print "one " + bin(~g)
  print "one " + bin(-~g)
  print "two " + bin(~-g)
  print bin(e)

  return g * e

def calc_2(data):
  oxy = ""
  co2 = ""

  l = len(data[0])
  for i in range(0, l):
    ones = 0
    for d in data:
      if d.startswith(oxy):
        print "%s starts with %s" % (d, oxy)
        ones += int(d[i])
    f = [d for d in data if d.startswith(oxy)]
    print(f)
    print(ones)
    if ones >= len(f) - ones:
      oxy += "1"
      print "Ones"
    else:
      oxy += "0"
      print "Zeros"

  l = len(data[0])
  for i in range(0, l):
    ones = 0
    for d in data:
      if d.startswith(co2):
        print "%s starts with %s" % (d, co2)
        ones += int(d[i])
    f = [d for d in data if d.startswith(co2)]
    if len(f) == 1:
      co2 = f[0]
      break
    print(f)
    print(ones)
    if ones >= len(f) - ones:
      co2 += "0"
      print "Zeros"
    else:
      co2 += "1"
      print "Ones"
      
    
  print("Oxy: %s" % oxy)
  print("Co2: %s" % co2)
    
  return int(oxy, 2) * int(co2, 2)

if __name__ == '__main__':
  print "One: %s" % calc_1(map(lambda x: x.rstrip(), open('data').readlines()))
  print "Two: %s" % calc_2(map(lambda x: x.rstrip(), open('data').readlines()))

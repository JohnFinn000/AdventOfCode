
def calc_1(data):
  h = 0
  v = 0
  for d in data:
    tup = d.split(" ")
    if tup[0] == "forward":
      h += int(tup[1])
    elif tup[0] == "down":
      v += int(tup[1])
    elif tup[0] == "up":
      v -= int(tup[1])
  
  return h * v

def calc_2(data):
  h = 0
  v = 0
  a = 0
  for d in data:
    tup = d.split(" ")
    if tup[0] == "forward":
      h += int(tup[1])
      v += int(tup[1]) * a
    elif tup[0] == "down":
      a += int(tup[1])
    elif tup[0] == "up":
      a -= int(tup[1])
  
  return h * v

if __name__ == '__main__':
  print "One: %s" % calc_1(map(lambda x: x.rstrip(), open('data').readlines()))
  print "Two: %s" % calc_2(map(lambda x: x.rstrip(), open('data').readlines()))

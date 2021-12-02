

def calc(data):
  return sum(1 for l, r in zip(data, data[1:]) if l < r)

if __name__ == '__main__':
  print calc(map(lambda x: int(x.rstrip()), open('data_1').readlines()))

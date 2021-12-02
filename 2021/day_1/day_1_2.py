
def calc(data):
    return sum(1 for index in range(len(data)-3) if sum(data[index:index+3]) < sum(data[index+1:index+4]))

if __name__ == '__main__':
  print calc(map(lambda x: int(x.rstrip()), open('data_1').readlines()))


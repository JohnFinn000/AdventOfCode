
def calc(data)
  first = data[0..2].sum
  second = data[1..3].sum
  count = 0
  for d in (4 ... data.size) do
    count += 1 if first < second
    first -= data[d-4]
    first += data[d-1]
    second -= data[d-3]
    second += data[d]
  end
  count += 1 if first < second
  count
end

if __FILE__ == $0
  puts calc File.open("data_1").readlines.map(&:to_i)
end

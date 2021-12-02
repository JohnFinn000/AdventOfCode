
def calc(data)
  data.zip(data.drop(1)).select { |l, r| !r.nil? &&l < r }.count
end

if __FILE__ == $0
  puts calc File.open("data_1").readlines
end

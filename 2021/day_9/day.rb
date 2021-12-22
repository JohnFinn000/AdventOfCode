require 'set'

def calc(data)
  risk = 0
  data_map = {}
  data.each_with_index { |row, y|
    row = row.strip
    row.each_char.with_index { |value, x|
      data_map[[x,y]] = value.to_i
    }
  }
  max_y = data.size
  max_x = data[0].strip.size
  risk = 0
  max_y.times { |y|
    max_x.times { |x|
      low_point = true
      [[x-1, y], [x+1, y], [x, y-1], [x, y+1]].each { |tup|
        if not data_map.key?(tup)
          next
        end
        if data_map[tup] <= data_map[[x, y]]
          low_point = false
          break
        end
      }
      if low_point
        risk += 1 + data_map[[x,y]]
      end
    }
  }
  risk
end

def calc_2(data)
  data_map = {}
  data.each_with_index { |row, y|
    row = row.strip
    row.each_char.with_index { |value, x|
      data_map[[x,y]] = value.to_i
    }
  }
  basin = {}
  basins = []
  max_y = data.size
  max_x = data[0].size
  max_y.times { |y|
    max_x.times { |x|
      if data_map[[x, y]] == 9
        next
      elsif basin.key?([x,y])
        next
      end
      basin[[x,y]] = 1
      basin_size = 1
      queue = Set[[x-1, y], [x+1, y], [x, y-1], [x, y+1]]     
      while queue.size > 0 do
        me = queue.to_a.last
        queue.delete(me)
        if not data_map.key?(me)
          next
        elsif data_map[me] == 9
          next
        elsif basin.key?(me)
          next
        else
          basin_size += 1
          basin[me] = 1
          xa, ya = me[0], me[1]
          [[xa-1, ya], [xa+1, ya], [xa, ya-1], [xa, ya+1]].each { |v|
            queue.add(v)
          }
        end
      end
      basins.append(basin_size) 
    }
  }
  basins = basins.sort.reverse
  answer = 1
  basins[0..2].each { |b|
    answer *= b
  }
  answer
end
    


describe "Advent of code tests pass" do
    let(:sample) {[
"2199943210",
"3987894921",
"9856789892",
"8767896789",
"9899965678",
]}

  context "first" do
    it "Processes sample properly" do
      expect(calc sample).to eq(15)
    end

    it "Processes file" do
      expect(calc File.open("data").readlines).to eq(475)
    end
  end

  context "second" do
    it "Processes sample properly" do
      expect(calc_2 sample).to eq(1134)
    end

    it "Processes file" do
      expect(calc_2 File.open("data").readlines).to eq(1092012)
    end
  end
end



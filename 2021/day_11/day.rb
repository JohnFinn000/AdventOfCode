require 'set'

def step(data)
  flash = Set[]

  max_y = data.size
  max_x = data[0].size
  max_y.times { |y|
    max_x.times { |x|
      data[y][x] += 1
      if data[y][x] > 9
        flash.add([x,y])
      end
    }
  }

  flashed = Set[]
  while flash.size > 0
    f = flash.to_a.pop
    flash.delete(f)
    flashed.add(f)
    [-1,0,1].each { |x|
      [-1,0,1].each { |y|
        if x == 0 and y == 0
          next
        end
        xa = f[0]+x
        ya = f[1]+y
        if xa < 0 or ya < 0
          next
        elsif xa >= max_x or ya >= max_y
          next
        end
        data[ya][xa] += 1
        if data[ya][xa] > 9
          if not flashed.include?([xa, ya])
            flash.add([xa, ya])
          end
        end
      }
    }
  end
  flashed.each { |f| data[f[1]][f[0]] = 0 }
  return data, flashed.size
end

def cleanup_data(data)
  cleaned_data = []
  data.each { |row|
    r = []
    row.strip.each_char { |c|
      r.append(c.to_i)
    }
    cleaned_data.append(r)
  }
  cleaned_data
end

def calc(data)
  data = cleanup_data(data)
  flashes = 0
  100.times { |s|
    data, flash_count = step(data)
    flashes += flash_count
  }
  flashes
end

def calc_2(data)
  data = cleanup_data(data)
  s = 1
  while true
    data, flash_count = step(data)
    if flash_count == 100
      break
    end
    s += 1
  end
  s
end


describe "Advent of code tests pass" do

  context "first" do
    it "Processes sample properly" do
      expect(calc File.open("sample").readlines).to eq(1656)
    end

    it "Processes file" do
      expect(calc File.open("data").readlines).to eq(1732)
    end
  end

  context "second" do
    it "Processes sample properly" do
      expect(calc_2 File.open("sample").readlines).to eq(195)
    end

    it "Processes file" do
      expect(calc_2 File.open("data").readlines).to eq(290)
    end
  end
end



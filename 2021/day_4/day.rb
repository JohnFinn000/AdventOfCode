
$row = "11111".to_i(2)
$col = ("00001"*5).to_i(2)

def bb_validate(bb)
  5.times { |i|
    [$row << 5*i, $col << i].each { |mask|
      return true if bb & mask == mask
    }
  }
  false
end

def bb_coord(coords)
  return 1 << coords[0] + (coords[1] * 5)
end

def bb_print(bb)
  5.times { |i|
    puts "%05b" % (bb & $row)
    bb >>= 5
  }
end

def calc(data)
  picks = data[0].split(',').map(&:to_i)
  data.shift

  boards, bitboards = [], []
  data.each_slice(6) { |b|
    b.shift
    boards.append(Hash.new)
    bitboards.append(0)
    b.each_with_index { |l, y|
      l.split.each_with_index { |n, x|
        boards[-1][n.to_i] = [x, y]
      }
    }
  }

  picks.each { |p|
    boards.each_with_index { |b, i|
      if b.key?(p)
        bitboards[i] |= bb_coord(b[p])
        b.delete(p)
      end
      if bb_validate(bitboards[i])
        return b.each_key.sum * p
      end
    }
  }
  
end

def calc_2(data)
  picks = data[0].split(',').map(&:to_i)
  data.shift

  boards, bitboards = [], []
  data.each_slice(6) { |b|
    b.shift
    boards.append(Hash.new)
    bitboards.append(0)
    b.each_with_index { |l, y|
      l.split.each_with_index { |n, x|
        boards[-1][n.to_i] = [x, y]
      }
    }
  }

  final_score = 0
  picks.each { |p|
    boards.each_with_index { |b, i|
      next if bb_validate(bitboards[i])
      if b.key?(p)
        bitboards[i] |= bb_coord(b[p])
        b.delete(p)
      end
      if bb_validate(bitboards[i])
        final_score = b.each_key.sum * p
      end
    }
  }
  final_score
end

describe "day 1 1 passes" do
    let(:sample) {[
"7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
"",
"22 13 17 11  0",
 "8  2 23  4 24",
"21  9 14 16  7",
 "6 10  3 18  5",
 "1 12 20 15 19",
"",
 "3 15  0  2 22",
 "9 18 13 17  5",
"19  8  7 25 23",
"20 11 10 24  4",
"14 21 16 12  6",
"",
"14 21 17 24  4",
"10 16 15  9 19",
"18  8 23 26 20",
"22 11 13  6  5",
 "2  0 12  3  7",
]}

  context "first" do
    it "Processes sample properly" do
      expect(calc sample).to eq(4512)
    end

    it "Processes file" do
      expect(calc File.open("data").readlines).to eq(67716)
    end
  end

  context "second" do
    it "Processes sample properly" do
      expect(calc_2 sample).to eq(1924)
    end

    it "Processes file" do
      expect(calc_2 File.open("data").readlines).to eq(1830)
    end
  end
end



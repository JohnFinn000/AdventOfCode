
def calc(data)
  crabs = data.split(',').map(&:to_i)
  crab_count = Hash.new(0)
  crabs.each { |c| crab_count[c] += 1 }
  best_cost = 999999
  (crabs.min..crabs.max).each { |p|
    cost = 0
    crab_count.each { |k, v|
      cost += (k-p).abs * v
    }
    best_cost = [cost, best_cost].min
  }
  best_cost
end

def calc_2(data)
  crabs = data.split(',').map(&:to_i)
  crab_count = Hash.new(0)
  crabs.each { |c| crab_count[c] += 1 }
  best_cost = 999999
  (crabs.min..crabs.max).each { |p|
    cost = 0
    crab_count.each { |k, v|
      d = (k-p).abs
      cost += (((d+1)*d)/2) * v
    }
    best_cost = [cost, best_cost].min
  }
  best_cost
end

describe "Advent of code tests pass" do
    let(:sample) {"16,1,2,0,4,2,7,1,2,14"}

  context "first" do
    it "Processes sample properly" do
      expect(calc sample).to eq(37)
    end

    it "Processes file" do
      expect(calc File.open("data").readlines[0]).to eq(349769)
    end
  end

  context "second" do
    it "Processes sample properly" do
      expect(calc_2 sample).to eq(168)
    end

    it "Processes file" do
      expect(calc_2 File.open("data").readlines[0]).to eq(99540554)
    end
  end
end



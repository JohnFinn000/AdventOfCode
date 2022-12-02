
def calc(data)
  data.to_a
  data.map!(&:strip)
  elves = data.slice_when{ |l, r| l == "" }
  elves = elves.map { |e| e.reject{|v| v == ""} }
  elves = elves.map { |e| e.map(&:to_i)}
  elves.map { |e| e.sum }.sort.reverse
end

def calc1(data)
  calc(data)[0]   
end

def calc2(data)
  calc(data)[0..2].sum
end

def read_sample()
  File.open("sample_1").readlines
end

def read_data()
  File.open("data").readlines
end

describe "Advent of code tests pass" do

  context "first" do
    it "Processes sample properly" do
      expect(calc1 read_sample).to eq(24000)
    end

    it "Processes file" do
      expect(calc1 read_data).to eq(69836)
    end
  end

  context "second" do
    it "Processes sample properly" do
      expect(calc2 read_sample).to eq(45000)
    end

    it "Processes file" do
      expect(calc2 read_data).to eq(207968)
    end
  end
end




def calc(data)
  
end

def calc_2(data)
  m = Hash.new(0)
  data.each { |d| 
    x1, y1, x2, y2 = d.match(/(\d+),(\d+) -> (\d+),(\d+)/).captures.map(&:to_i)
    d = [(x2-x1).abs, (y2-y1).abs].max + 1
    x = x2 <=> x1
    y = y2 <=> y1
    d.times { |i| m[[x1+x*i, y1+y*i]] += 1 }
  }
  m.select { |k, v| v > 1 }.keys.count
end


describe "day 1 1 passes" do
    let(:sample) {[
"0,9 -> 5,9",
"8,0 -> 0,8",
"9,4 -> 3,4",
"2,2 -> 2,1",
"7,0 -> 7,4",
"6,4 -> 2,0",
"0,9 -> 2,9",
"3,4 -> 1,4",
"0,0 -> 8,8",
"5,5 -> 8,2",
]}

  context "first" do
    xit "Processes sample properly" do
      expect(calc sample).to eq(5)
    end

    xit "Processes file" do
      expect(calc File.open("data").readlines).to eq(7436)
    end
  end

  context "second" do
    it "Processes sample properly" do
      expect(calc_2 sample).to eq(12)
    end

    it "Processes file" do
      expect(calc_2 File.open("data").readlines).to eq(21104)
    end
  end
end



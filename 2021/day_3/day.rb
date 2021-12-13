
# TODO This solution wasn't finished.
def calc(data)
  l = data[0].length
  bit = 1 << l - 1
  e = 0
  g = 0
  l.times {
    e <<= 1
    g <<= 1
    if data.count { |d| d.to_i(2) & bit > 0 } >= data.length/2
      e |= 1
    else
      g |= 1
    end
    bit >>= 1
  }
  mask = 0
  l.times {
    mask <<= 1
    mask |= 1
  }
  puts e.to_s(2)
  puts e
  puts (mask ^ e).to_s(2)
  puts (mask ^ e)
  puts "g: #{g}"
  e * (mask ^ e)
end

def calc_2(data)
  0
end

describe "day 1 1 passes" do
    let(:sample) {[
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010",
]}

  context "first" do
    xit "Is 0 when empty" do
      expect(calc []).to eq(0)
    end

    it "Processes sample properly" do
      expect(calc sample).to eq(198)
    end

    #it "Processes sample properly" do
    #  expect(calc sample).to eq(198)
    #end

    it "Processes file" do
      expect(calc File.open("data").readlines).to eq(3885894)
    end
  end

  #context "second" do
  #  it "Is 0 when empty" do
  #    expect(calc_2 []).to eq(0)
  #  end

  #  it "Processes sample properly" do
  #    expect(calc_2 sample).to eq(900)
  #  end

  #  it "Processes file" do
  #    expect(calc_2 File.open("data").readlines).to eq(2006917119)
  #  end
  #end
end



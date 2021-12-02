
def calc(data)
  horizontal = 0
  vertical = 0
  data.each { |c| 
    command, value = c.split
    case command
    when "forward"
     horizontal += value.to_i
    when "up"
     vertical -= value.to_i
    when "down"
     vertical += value.to_i
    end
  }
  return horizontal * vertical
end

def calc_2(data)
  horizontal = 0
  vertical = 0
  aim = 0
  data.each { |c| 
    command, value = c.split
    case command
    when "forward"
     horizontal += value.to_i
     vertical += aim * value.to_i
    when "up"
     aim -= value.to_i
    when "down"
     aim += value.to_i
    end
  }
  return horizontal * vertical
end

describe "day 1 1 passes" do
    let(:sample) {[
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2",
]}

  context "first" do
    it "Is 0 when empty" do
      expect(calc []).to eq(0)
    end

    it "Processes sample properly" do
      expect(calc sample).to eq(150)
    end

    it "Processes file" do
      expect(calc File.open("data").readlines).to eq(1989014)
    end
  end

  context "second" do
    it "Is 0 when empty" do
      expect(calc_2 []).to eq(0)
    end

    it "Processes sample properly" do
      expect(calc_2 sample).to eq(900)
    end

    it "Processes file" do
      expect(calc_2 File.open("data").readlines).to eq(2006917119)
    end
  end
end


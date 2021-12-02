require_relative 'day_1_2'

describe "day 1 2 passes" do
  it "Is 0 when empty" do
    expect(calc [0]).to eq(0)
  end

  it "Processes sample properly" do
    data = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    expect(calc data).to eq(5)
  end
end

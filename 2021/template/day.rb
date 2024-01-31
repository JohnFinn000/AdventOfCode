
def calc(data)
  
end

def calc2(data)
  
end


describe "Advent of code tests pass" do
    let(:sample) {[
]}

  context "first" do
    it "Processes sample properly" do
      expect(calc File.open('sample').readlines).to eq(0)
    end

    xit "Processes file" do
      expect(calc File.open("data").readlines).to eq(0)
    end
  end

  context "second" do
    xit "Processes sample properly" do
      expect(calc2 File.open('sample').readlines).to eq(0)
    end

    xit "Processes file" do
      expect(calc2 File.open("data").readlines).to eq(0)
    end
  end
end



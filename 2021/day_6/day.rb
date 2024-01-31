
def calc(data)
  
end

def calc_2(data)
end


describe "day 1 1 passes" do
    let(:sample) {[
"3,4,3,1,2"
]}

  context "first" do
    it "Processes sample properly" do
      expect(calc sample).to eq(5934)
    end

    xit "Processes file" do
      expect(calc File.open("data").readlines).to eq(391671)
    end
  end

  context "second" do
    xit "Processes sample properly" do
      expect(calc_2 sample).to eq(26984457539)
    end

    xit "Processes file" do
      expect(calc_2 File.open("data").readlines).to eq(1754000560399)
    end
  end
end



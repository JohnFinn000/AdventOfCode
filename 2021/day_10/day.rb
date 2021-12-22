
def calc(data)
    opens = '[({<'
    matches = {
        '['=> ']',
        '('=> ')',
        '{'=> '}',
        '<'=> '>',
        ']'=> '[',
        ')'=> '(',
        '}'=> '{',
        '>'=> '<',
    }
    points = {
        ')'=> 3,
        ']'=> 57,
        '}'=> 1197,
        '>'=> 25137,
    }
    point_count = 0
    data.each { |d|
      stack = []
      d.strip.each_char { |c|
        if opens.include?(c)
          stack.append(c)
        else
          if stack[-1] == matches[c]
            stack.pop
          else
            point_count += points[c]
            break
          end
        end
      }
    }
    point_count
end

def calc2(data)
    opens = '[({<'
    matches = {
        '['=> ']',
        '('=> ')',
        '{'=> '}',
        '<'=> '>',
        ']'=> '[',
        ')'=> '(',
        '}'=> '{',
        '>'=> '<',
    }
    points = {
        ')'=> 1,
        ']'=> 2,
        '}'=> 3,
        '>'=> 4,
    }
    scores = []
    data.each { |d|
      stack = []
      d.strip.each_char { |c|
        if opens.include?(c)
          stack.append(c)
        else
          if stack[-1] == matches[c]
            stack.pop
          else
            stack = []
            break
          end
        end
      }
      if stack.empty?
        next
      end
      point_count = 0
      stack.reverse_each { |s|
        point_count *= 5
        point_count += points[matches[s]]
      }
      scores.append(point_count)
    }
    scores.sort[scores.size/2]
end


describe "Advent of code tests pass" do
    let(:sample) {[
"[({(<(())[]>[[{[]{<()<>>",
"[(()[<>])]({[<{<<[]>>(",
"{([(<{}[<>[]}>{[]{[(<()>",
"(((({<>}<{<{<>}{[]{[]{}",
"[[<[([]))<([[{}[[()]]]",
"[{[{({}]{}}([{[{{{}}([]",
"{<[[]]>}<{[{[{[]{()[[[]",
"[<(<(<(<{}))><([]([]()",
"<{([([[(<>()){}]>(<<{{",
"<{([{{}}[<[[[<>{}]]]>[]]",
]}

  context "first" do
    it "Processes sample properly" do
      expect(calc sample).to eq(26397)
    end

    it "Processes file" do
      expect(calc File.open("data").readlines).to eq(318099)
    end
  end

  context "second" do
    it "Processes sample properly" do
      expect(calc2 sample).to eq(288957)
    end

    it "Processes file" do
      expect(calc2 File.open("data").readlines).to eq(2389738699)
    end
  end
end



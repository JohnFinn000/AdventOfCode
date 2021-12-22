import unittest
import re
from collections import defaultdict
from collections import Counter
from numpy import sign

def calc(data):
    opens = '[({<'
    matches = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>',
        ']': '[',
        ')': '(',
        '}': '{',
        '>': '<',
    }
    points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
    }
    point_count = 0
    for d in data:
        #print d
        stack = []
        for c in d.strip():
            #print stack
            if c in opens:
                stack.append(c)
            else:
                if stack[-1] == matches[c]:
                    stack.pop()
                else:
                    point_count += points[c]
                    #print "%r does not match %r" % (c, stack[0])
                    break
            
    return point_count

def calc2(data):
    opens = '[({<'
    matches = {
        '[': ']',
        '(': ')',
        '{': '}',
        '<': '>',
        ']': '[',
        ')': '(',
        '}': '{',
        '>': '<',
    }
    points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
    }
    scores = []
    for d in data:
        #print d
        stack = []
        for c in d.strip():
            #print stack
            if c in opens:
                stack.append(c)
            else:
                if stack[-1] == matches[c]:
                    stack.pop()
                else:
                    #print "%r does not match %r" % (c, stack[0])
                    print 
                    stack = []
                    break
        if len(stack) == 0:
            print "Discarding %r %r" % (stack, d)
            continue
        print "Calculating score"
        print stack
        point_count = 0
        for s in stack[::-1]:
            point_count *= 5
            point_count += points[matches[s]]
        print point_count
        print scores
        scores.append(point_count)
    print "Scores %r" % scores
    scores.sort()
    return scores[len(scores)/2]

class TestDay(unittest.TestCase):
    sample = [
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
]

    def test_first_sample_data(self):
        self.assertEqual(calc(self.sample), 26397)

    def test_first_final_data(self):
        self.assertEqual(calc(open('data').readlines()), 318099)

    def test_second_challenge_sample(self):
        self.assertEqual(calc2(self.sample), 288957)

    def test_second_final_data_2(self):
        self.assertEqual(calc2(open('data').readlines()), 2389738699)

if __name__ == '__main__':
    unittest.main()

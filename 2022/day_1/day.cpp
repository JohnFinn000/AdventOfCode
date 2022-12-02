//#include <stdlib.h>
//#include <iostream>
#include <gtest/gtest.h>
#include <fstream>
#include <numeric>

using namespace std;

std::vector<int> calc(std::vector<string> data) {
    std::vector<int> elves;
    int calories = 0;
    for(string line : data) {
        try {
            calories += stoi(line);
        } catch (std::invalid_argument e) {
            elves.push_back(calories);
            calories = 0;
        }
    }
    sort(elves.begin(), elves.end(), greater <>());
    return elves;
}

int calc1(std::vector<string> data) {
    return calc(data)[0];
}

int calc2(std::vector<string> data) {
    auto elves = calc(data);
    return std::reduce(elves.begin(), elves.begin() + 3);
}

std::vector<string> read_file(string filename) {
    fstream f;
    f.open(filename, ios::in);
    if(!f) {
        throw "Could not open file";
    }
    std::vector<string> lines;
    for(string line; getline(f, line);) {
        lines.push_back(line);
    }
    return lines;
}

std::vector<string> read_sample() {
    return read_file("sample_1");
}

std::vector<string> read_data() {
    return read_file("data");
}

TEST(TestSuite, Sample1) {
    EXPECT_EQ(calc1(read_sample()), 24000);
}

TEST(TestSuite, Data1) {
    EXPECT_EQ(calc1(read_data()), 69836);
}

TEST(TestSuite, Sample2) {
    EXPECT_EQ(calc2(read_sample()), 41000);
}

TEST(TestSuite, Data2) {
    EXPECT_EQ(calc2(read_data()), 207968);
}

int main(int argc, char **argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}

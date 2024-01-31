package main

import (
    "testing"
    "os"
    "fmt"
    "strings"
)

func calc1(data string) int {
    fmt.Println(strings.Fields(data))
    return 1
}

func calc2(data string) int {
    fmt.Println(strings.Fields(data))
    return 1
}

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func read_sample() string {
    dat, err := os.ReadFile("sample_1")
    check(err)
    return string(dat)
}

func read_data() string {
    dat, err := os.ReadFile("data")
    check(err)
    return string(dat)
}

func TestCalc1(t *testing.T) {
    fmt.Printf("Testing Calc1 Sample")
    results := calc1(read_sample())
    fmt.Print(results)
    if results != 1 {
        t.Errorf("got: %d, wanted: %d", results, 1)
        return
    }

    fmt.Printf("Testing Calc1 Data")
    results = calc1(read_data())
    fmt.Print(results)
    if results != 1 {
        t.Errorf("got: %d, wanted: %d", results, 1)
        return
    }
}

//func TestCalc2(t *testing.T) {
//    fmt.Printf("Testing Calc2 Sample")
//    results := calc2(read_sample())
//    fmt.Print(results)
//    if results != 1 {
//        t.Errorf("got: %d, wanted: %d", results, 1)
//        return
//    }
//
//    fmt.Printf("Testing Calc2 Data")
//    results = calc2(read_data())
//    fmt.Print(results)
//    if results != 1 {
//        t.Errorf("got: %d, wanted: %d", results, 1)
//        return
//    }
//}

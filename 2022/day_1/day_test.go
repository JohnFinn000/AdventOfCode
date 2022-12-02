package main

import (
    "testing"
    "os"
    "fmt"
    "strings"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func calc1(data string) int {
    fmt.Println(strings.Fields(data))
    return 1
}

func read_sample() string {
    dat, err := os.ReadFile("sample_1")
    check(err)
    return string(dat)
}

func TestCalc1(t *testing.T) {
    fmt.Printf("Testing")
    fmt.Print(calc1(read_sample()))
    //t.Errorf("got: %d, want: %d", calc1(), 1)
}

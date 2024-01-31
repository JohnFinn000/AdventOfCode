package main

import (
        "fmt"
        "io/ioutil"
        "strconv"
        "strings"
)

func calc_fuel(mass int) int {
        var fuel int 
        for {
                new_fuel := (mass / 3) - 2 
                if new_fuel < 0 { 
                        break
                }
                fuel += new_fuel
                mass = new_fuel                                                                                                                                                                                                                                                                                                                  
        }
        return fuel
}

func check(e error) {
        if e != nil {
                panic(e)
        }
}

func main() {
        dat, err := ioutil.ReadFile("1_input.txt")
        check(err)
        mass_list := strings.Split(string(dat), "\n")
        var total_fuel int = 0 
        for i := 0; i < len(mass_list); i++ {
                fmt.Printf("\"%s\"\n", mass_list[i])
                num, err := strconv.Atoi(mass_list[i])
                if err != nil {
                        continue
                }
                total_fuel += calc_fuel(num)
        }
        fmt.Printf("Total fuel: %d\n", total_fuel)
}

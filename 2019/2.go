package main

import (
        "fmt"
        "io/ioutil"
        "strconv"
        "strings"
)

func check(e error) {
        if e != nil {
                panic(e)
        }
}

func calculate_all_operands(memory map[int]int, code_int_list []int, one int, two int) int {
        memory[1] = one 
        memory[2] = two 

        for i := 0; i < len(code_int_list); i += 4 { 
                opcode := code_int_list[i]
                if opcode == 99 {
                        break
                }
                left := code_int_list[i+1]
                right := code_int_list[i+2]
                result := code_int_list[i+3]
                if opcode == 1 { 
                        //fmt.Printf("%d = %d + %d\n", memory[result], memory[left], memory[right])
                        memory[result] = memory[left] + memory[right]
                }
                if opcode == 2 { 
                        //fmt.Printf("%d = %d * %d\n", memory[result], memory[left], memory[right])
                        memory[result] = memory[left] * memory[right]
                }
        }
        return memory[0]
}

func calculate_intoperands(filepath string) int {
        dat, err := ioutil.ReadFile(filepath)
        check(err)
        sanitized_code_string := strings.TrimSpace(string(dat))
        code_list := strings.Split(sanitized_code_string, ",")
        //fmt.Print(code_list)
        var memory = make(map[int]int)
        code_int_list := []int{}
        for i := 0; i < len(code_list); i++ {
                num, err := strconv.Atoi(code_list[i])
                code_int_list = append(code_int_list, num)
                check(err)
                memory[i] = num 
        }

        for left := 1; left <= 99; left++ {
                for right := 1; right <= 99; right++ {
                        result := calculate_all_operands(memory, code_int_list, left, right)
                        if result == 19690720 {
                                return left*100 + right
                        }
                }
        }
        return 0
}

func main() {
        fmt.Printf("Code: %d\n", calculate_intoperands("2_input.txt"))
}
